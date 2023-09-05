import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request

app = Flask(__name__)

# Set GPIO numbering mode
GPIO.setmode(GPIO.BCM)

# Set pin 25 as an output, and define it as the servo PWM pin
GPIO.setup(25, GPIO.OUT)
servo = GPIO.PWM(25, 50)  # Pin 25 for servo, pulse 50Hz
servo.start(0)  # Start servo at 0 degrees

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move_servo', methods=['POST'])
def move_servo():
    angle = request.form['angle']
    angle = float(angle)
    duty_cycle = 2 + (angle / 18)
    servo.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)
    return 'OK'

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=8080, debug=True)
    finally:
        servo.stop()
        GPIO.cleanup()
        app.run(host='0.0.0.0', port=8080, debug=True)
    
