import numpy as np


def calc_angles(x, y, h):
    '''
    Given an x and a y coordinate wrt the nozzle rotation axis, and the height of the nozzle, calculate the angles to send to the servo

    x (float): meters from the nozzle on the x axis (right is positive)
    y (float): meters from the nozzle on the y axis (should only be positive for now)
    h (float): height from the ground of the nozzle in meters
    '''
    yaw_ang = np.arctan(y/x) *360/(2*np.pi)
    pitch_ang = 0

    return yaw_ang, pitch_ang

print(calc_angles(-3, 6, 0))