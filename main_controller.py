from GUI import LawnGUI
from dual_servo_actuator import ServoControl
import math
from scipy.optimize import fsolve
import time

 
class MainController:
    def __init__(self, v0, h):
        self.gui = LawnGUI()
        self.servo_control = ServoControl()
        self.v0 = v0  # Initial velocity of the water
        self.h = h    # Height of the hose from the floor
 
    def calculate_horizontal_angle(self, x, y):
        """Calculate the horizontal angle to point at the target (x, y)."""
        # Calculate angle_x using the arctangent of the horizontal distances
        angle_x = math.degrees(math.atan2(y, x))  # Angle in degrees
        return angle_x
 
    def projectile_motion_calculation(self, x, y):
        """Calculate the launch angle required to hit a target at (x, y)."""
        g = 9.81  # Gravity
 
        def equations(theta):
            """Equation to solve for vertical angle theta."""
            theta_rad = math.radians(theta)
            t = x / (self.v0 * math.cos(theta_rad))  # Time of flight based on horizontal distance
            y_calc = self.h + self.v0 * math.sin(theta_rad) * t - (0.5 * g * t**2)
            return y_calc - y
 
        # Solve for theta using fsolve
        theta_solution = fsolve(equations, 45)[0]  # Start with an initial guess of 45 degrees
        return theta_solution
 
    def get_and_process_coordinates(self):
        # Run the GUI to allow user interaction and selection
        self.gui.run()
        # Retrieve coordinates after user interaction and submission
        coordinates = self.gui.selected_coordinates
        # Calculate angles based on coordinates and move servos sequentially
        for x, y in coordinates:
            # Calculate both horizontal and vertical angles
            angle_x = self.calculate_horizontal_angle(x, y)
            angle_y = self.projectile_motion_calculation(x, y)
            # Move servos to the calculated angles
            self.servo_control.move_servos(angle_x, angle_y)
            time.sleep(2)
 
    def run(self):
        self.get_and_process_coordinates()
