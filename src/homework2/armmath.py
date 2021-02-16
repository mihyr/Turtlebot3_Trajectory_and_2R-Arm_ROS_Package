#!/usr/bin/env python
from math import sin, cos, sqrt, pi, acos, asin, atan2

def xy_coordinates(time, L1, L2, total_time):
    h = 2/3*(L1+L2)
    x = 0.9*cos(2*pi*time/total_time)*sqrt((L1+L2)**2-h**2)
    y = h
    return x, y

def joint_angles(x,y,L1,L2):
    alpha = acos((x**2+y**2+L1**2-L2**2)/2*L1*sqrt(x**2+y**2))
    beta = acos((L1**2 + L2**2 - x**2 - y**2)/2*L1*L2)
    gamma = atan2(y,x)
    theta1 = gamma - alpha
    theta2 = pi - beta
    return theta1, theta2