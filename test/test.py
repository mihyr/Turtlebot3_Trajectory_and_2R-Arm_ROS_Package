#!/usr/bin/env python
import unittest
from homework2.trajectorymath import traj_coordinates, xy_derivatives
from homework2.armmath import xy_coordinates, joint_angles

class MyTestCase(unittest.TestCase):

    def __init__(self, *args):
        super(MyTestCase, self).__init__(*args)
        self.H = 2.0
        self.W = 4.0
        self.T = 80
        self.total_time = 10
        self.L1 = 0.8
        self.L2 = 0.6
    
    #Figure 8 Test
    def traj_coordinates(self):
        time = 1.0
        x_coor, y_coor  = traj_coordinates(self.H,self.W,time,self.T)

        self.assertAlmostEqual(x_coor, 0.1569, 2, 0.05)
        self.assertAlmostEqual(y_coor, 0.1564, 2, 0.05)

    def xy_derivatives(self):
        x_coor = 2
        y_coor = 3
        time = 1.0
        v_linear, v_angular, theta = xy_derivatives(x_coor,y_coor,self.H,self.W,time,self.T)

        self.assertAlmostEqual(v_linear, 0.2204, 4, 0.05)
        self.assertAlmostEqual(v_angular, -0.0934, 4, 0.05)
        self.assertAlmostEqual(theta, 0.7807, 4, 0.05)

    #2R ARM Test

    def xy_coordinates(self):
        time = 2.0
        x_coor, y_coor = xy_coordinates(time, self.L1, self.L2, self.total_time, 4, 0.05)

        self.assertAlmostEqual(x_coor, 0.29021 , 4, 0.05)
        self.assertAlmostEqual(y_coor, 0.93333, 4, 0.05)

    def joint_angles(self):
        x_coor = 1
        y_coor = 2
        theta1, theta2 = joint_angles(x_coor, y_coor, self.L1, self.L2)

        self.assertAlmostEqual(theta1, 0.60922, 4, 0.05)
        self.assertAlmostEqual(theta2, 1.61733, 4, 0.05)

if __name__ == "__main__":
    import rosunit
    rosunit.unitrun(homework2, 'test', MyTestCase)