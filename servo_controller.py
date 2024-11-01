import RPi.GPIO as GPIO
import time
from angle_provider import AngleProvider  # Importing AngleProvider from angle_provider.py

class ServoControl:
    def __init__(self):
        # Set up GPIO mode
        GPIO.setmode(GPIO.BOARD)
        
        # Define GPIO pins for the servos
        self.servo_x_pin = 11  # X-axis servos connected to pin 11
        self.servo_y_pin = 13  # Y-axis servo connected to pin 13

        # Set the GPIO pin mode to output
        GPIO.setup(self.servo_x_pin, GPIO.OUT)
        GPIO.setup(self.servo_y_pin, GPIO.OUT)

        # Create PWM objects for the servos (50 Hz frequency)
        self.pwm_x = GPIO.PWM(self.servo_x_pin, 50)
        self.pwm_y = GPIO.PWM(self.servo_y_pin, 50)

        # Start PWM with 0% duty cycle
        self.pwm_x.start(0)
        self.pwm_y.start(0)

    def set_servo_angle(self, pwm, angle):
        # Calculate duty cycle from angle (2% to 12% duty cycle = 0 to 180 degrees)
        duty_cycle = 2 + (angle / 18)
        pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(0)

    def move_servos(self, angle_x, angle_y):
        # Limit angle_y to 0-30 degrees
        angle_y = max(0, min(angle_y, 30))
        
        # Move servos to angles
        self.set_servo_angle(self.pwm_x, angle_x)
        self.set_servo_angle(self.pwm_y, angle_y)

    def cleanup(self):
        # Stop the PWM and cleanup GPIO on exit
        self.pwm_x.stop()
        self.pwm_y.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    angle_provider = AngleProvider() # CHANGE NAME - THIS IS JUST A PLACE HOLDER FOR THE CLASS FROM THE MASTER CONTROLLER
    servo_controller = ServoControl()
    
    try:
        while True:
            # Retrieve angles from AngleProvider instead of manual input
            angle_x, angle_y = angle_provider.get_angles()
            servo_controller.move_servos(angle_x, angle_y)
            time.sleep(1)  # Adjust time as needed
    except KeyboardInterrupt:
        servo_controller.cleanup()
