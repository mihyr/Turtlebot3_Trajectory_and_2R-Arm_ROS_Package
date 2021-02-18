#!/usr/bin/env python
from math import sin, cos, sqrt, pi, acos, asin, atan2

def xy_coordinates(time, L1, L2, total_time):
    '''Calculates 2R arm trajectory coordinates
    Args:
        L1 - length of base link of 2R arm
        L2 - length of child link of 2R arm
        time - current time in ROS
        total_time - Time Period req for one loop (arm tracectory)
    Return:
        x,y - x and y coordinates of 2R arm trajectory
    '''
    
    #Trajectory Math
    h = 2/3*(L1+L2)
    x = 0.9*cos(2*pi*time/total_time)*sqrt((L1+L2)**2-h**2)
    y = h

    return x, y

def joint_angles(x,y,L1,L2):
    ''' Calculation for theta1 and theta2 for base and child link of 2R arms
    Reference: chapter 6- Lynch, Kevin M., and Frank C. Park. Modern Robotics. Cambridge University Press, 2017.

    Args:
        x,y - x and y coordinates of 2R arm trajectory
        L1 - length of base link of 2R arm
        L2 - length of child link of 2R arm
    Return:
        theta1, theta2 - joint angles of base and child link in radians
    '''

    alpha = acos((x**2+y**2+L1**2-L2**2)/(2*L1*sqrt(x**2+y**2)))
    beta = acos((L1**2 + L2**2 - x**2 - y**2)/(2*L1*L2))
    gamma = atan2(y,x)
    theta1 = gamma - alpha
    theta2 = pi - beta

    return theta1, theta2