# raspberry_pi_servo_motor_html
Raspberry Pi Servo Motor Angle Control with Flask This Python script allows you to control the angle of a servo motor using a Raspberry Pi through a web-based interface created with the Flask framework. The web page provides an input field to specify the servo angle and a button to move the servo to the specified angle
![raspberry_pi_servo_motor](https://github.com/qbi777/raspberry_pi_servo_motor_html/assets/123941775/557b274a-27a8-47ac-b638-8a1632aa36b7)

Note:
  Both servo.py and the templates files want to take place in the same folder.
  
![html_servo](https://github.com/qbi777/raspberry_pi_servo_motor_html/assets/123941775/0e92e1bd-2419-4b80-b595-f387cd9e1d98)

Before running this code, make sure you have the following components and software set up:
Raspberry Pi (any model with GPIO pins)
RPi.GPIO library (Python library for GPIO control)
Python 3
Flask library (for creating the web interface)

Explanation:

This Python script demonstrates how to control the angle of a servo motor using a Raspberry Pi with a web-based interface created using the Flask framework. It allows you to specify the angle of the servo and move it to that angle by accessing a specific URL in your web browser.

The script uses the RPi.GPIO library for Raspberry Pi GPIO control and the Flask library for creating a web server.
It sets up GPIO pin 25 as an output for controlling the servo motor.
The Flask app has two routes:
'/' : This route renders an HTML template called index.html, which contains an input field to specify the servo angle and a button to submit the angle.
'/move_servo': This route is used to move the servo to the specified angle by changing the duty cycle of the PWM signal.
