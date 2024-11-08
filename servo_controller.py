import RPi.GPIO as GPIO
import time

class ServoControl:
    def __init__(self):
        # Set up GPIO mode
        GPIO.setmode(GPIO.BOARD)

        # Define GPIO pins for the servos
        self.servo_x_pin = 11  # X-axis servo
        self.servo_y_pin = 13  # Y-axis servo

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
        """Convert angle to duty cycle and move the servo."""
        duty_cycle = 2 + (angle / 18)
        pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(0)  # Stop PWM to avoid jitter

    def move_servos(self, angle_x, angle_y):
        """Move servos to specified angles."""
        angle_y = max(0, min(angle_y, 30))  # Limit Y-axis angle to 0-30 degrees
        self.set_servo_angle(self.pwm_x, angle_x)
        self.set_servo_angle(self.pwm_y, angle_y)

    def cleanup(self):
        """Stop the PWM and clean up GPIO on exit."""
        self.pwm_x.stop()
        self.pwm_y.stop()
        GPIO.cleanup()
   
    def run(self):
        """Run method if needed for continuous operation."""
        pass  # Placeholder for any continuous functionality
