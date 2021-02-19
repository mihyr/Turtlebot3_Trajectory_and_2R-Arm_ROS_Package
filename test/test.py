#!/usr/bin/env python
import unittest
import homework2
from homework2.trajectorymath import traj_coordinates, xy_derivatives
from homework2.armmath import xy_coordinates, joint_angles

class MyTestCase(unittest.TestCase):

    def xy_derivatives(self):
        
        v_linear, v_angular, theta = xy_derivatives(x_coor,y_coor,H,W,time,T)

        self.assertAlmostEqual(<expression1>, <expression2>)

    def traj_coordinates(self):

        x_coor, y_coor  = traj_coordinates(H,W,time,T)

        self.assertEquals(<expression1>, <expression2>)

    def xy_coordinates(self):
        
        x_coor, y_coor = xy_coordinates(time, L1, L2, total_time)

        self.assertAlmostEqual(<expression1>, <expression2>)

    def joint_angles(self):

        theta1, theta2 = joint_angles(x_coor, y_coor,L1,L2)

        self.assertAlmostEqual(<expression1>, <expression2>)

if __name__ == "__main__":
    import rosunit
    rosunit.unitrun(homework2, 'test', MyTestCase)