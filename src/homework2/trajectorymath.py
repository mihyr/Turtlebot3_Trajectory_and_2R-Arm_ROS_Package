#!/usr/bin/env python
from math import sin, cos, pi, atan
from numpy import arctan, sqrt

def traj_coordinates(h,w,current_time,total_time):
    '''Calculates figure 8 trajectory coordinates
    Args:
        h - height of figure 8
        w - width of figure 8
        current_time - current time in ROS
        total_time - time required to complete one complete figure 8 loop
    Return:
        x,y - x and y coordinates of figure 8 trajectory
    '''
    #Trajectory equation
    x = (w/2)*sin(2*pi*current_time/total_time)
    y = (h/2)*sin(4*pi*current_time/total_time)
    
    return x,y

def xy_derivatives(x,y,h,w,t,T):
    '''Calculates first and second order derivative of x and y and returns linear and angular velocity for figure 8 trajectory
    Args:
        x_dot, y_dot - first order derivative of x and y coordinates
        x_dd, y_dd - second order derivative of x and y coordinates
        h - Height of figure 8
        w - Width of figure 8
        t - current time in ROS
        T -time required to complete one complete figure 8 loop
    Return:
        Velocity: linear velocity (Vx)
        omega: Angular velocity (Y)
        theta: angle theta, used for calculating quat in world to odom transformation

    '''
    x_dot = (w*pi/T)*cos(2*pi*t/T)
    y_dot = (2*h*pi/T)*cos(4*pi*t/T)

    x_dd = -2*(pi**2/(T**2))*w*sin(2*pi*t/T)
    y_dd = -8*(pi**2/(T**2))*h*sin(4*pi*t/T) 
    
    velocity = sqrt(x_dot**2 + y_dot**2)
    omega = ((y_dd*x_dot)-(y_dot*x_dd))/((x_dot**2+y_dot**2))
    theta = atan(y_dot/x_dot)

    return velocity, omega, theta   