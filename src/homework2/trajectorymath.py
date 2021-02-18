#!/usr/bin/env python
from math import sin, cos, pi, atan2
from numpy import arctan, sqrt

def traj_coordinates(h,w,current_time,total_time):
    x = (w/2)*sin(2*pi*current_time/total_time)
    y = (h/2)*sin(4*pi*current_time/total_time)
    return x,y

def xy_derivatives(x,y,h,w,t,T):
    x_dot = (w*pi/T)*cos(2*pi*t/T)
    y_dot = (2*h*pi/T)*cos(4*pi*t/T)

    x_dd = -2*(pi**2/(T**2))*w*sin(2*pi*t/T)
    y_dd = -8*(pi**2/(T**2))*h*sin(4*pi*t/T) 
    
    velocity = sqrt(x_dot**2 + y_dot**2)
    omega = ((y_dd*x_dot)-(y_dot*x_dd))/((x_dot**2+y_dot**2))
    theta = atan2(y_dot,x_dot)

    return velocity, omega, theta