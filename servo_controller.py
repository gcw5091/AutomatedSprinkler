import RPi.GPIO as GPIO
import time

class ServoControl:
    def __init__(self):
        #Set up GPIO mode
        GPIO.setmode(GPIO.BOARD) # 1 2
                                 # 3 4
                                 # 5 ...
        # Define GPIO pins for the servos (based on BOARD numbering above)
        self.servo_x_pin = 11 # X-axis servos connected to pin 11 (GPIO17 in BCM)
        self.servo_y_pin = 13 # Y-axis servo connected to pin 13 (GPIO27 in BCM)

        # Set the GPIO pin mode to output
        GPIO.setup(self.servo_x_pin, GPIO.OUT)
        GPIO.setup(self.servo_y_pin, GPIO.OUT)

        #Create PWM objects for the servos (50 Hz freq) (I/O pins: 7,11,12,13,15,16,18,22)
        self.pwm_x = GPIO.PWM(self.servo_x_pin,50) # pin(11), frequency 50 Hz
        self.pwm_y = GPIO.PWM(self.servo_y_pin,50) # pin(13), frequency 50 Hz

        # Start PWM with 0% duty cycle (servos will not move initially)
        self.pwm_x.start(0)
        self.pwm_y.start(0)

    def set_servo_angle(self, pwm, angle): # Function to set servo angle (0 to 180 degrees)
        # Calculate duty cycle from angle (2% to 12% duty cycle = 0 to 180 degrees)
        duty_cycle = 2 + (angle/18)
        pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(0.5) # Allow time for servo to reach destination
        pwm.ChangeDutyCycle(0) # prevents jitter

    def move_servos(self, angle_x, angle_y):
        # Input angle for Y axis (limited from 0-30 degrees)
        if angle_y < 0:
            angle_y = 0
        elif angle_y > 30:
            angle_y = 30
        
        # Move servos to angles
        self.set_servo_angle(self.pwm_x, angle_x)
        self.set_servo_angle(self.pwm_y, angle_y)

    def cleanup(self):
        # stop the PWM and cleanup GPIO on exit
        self.pwm_x.stop()
        self.pwm_y.stop()
        GPIO.cleanup() # resets the state of the GPIO pins and return them to default st

# Example
if __name__ == "main":
    try:
        servo_controller = ServoControl()
        while True:
            # Get inputs of angles
            angle_x = float(input("Enter angle for X axis (0-180): "))
            angle_y = float(input("Enter angle for Y axis (0-30): "))

            #move
            servo_controller.move_servos(angle_x, angle_y)
    except KeyboardInterrupt:
        #cleanup everything
        servo_controller.cleanup()