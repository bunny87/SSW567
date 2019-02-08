# -*- coding: utf-8 -*-
"""
Updated on Tuesday Februrary 5, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: vineet singh

“I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment/examination. I further pledge that I have not copied
any material from a book, article, the Internet or any other source except where I
have expressly cited the source.”
"""

import unittest

from TriangleFixed import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangle(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3, 4, 5 is a Right triangle')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Scalene', '5, 3, 4 is a Scalene triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1, 1, 1 is an Equilateral triangle')

    def testIsocelesTriangle(self):
        self.assertEqual(classifyTriangle(3, 5, 5), 'Isoceles', '3, 5, 5 is a Isoceles triangle')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(4, 2, 1), 'NotATriangle', '4, 2, 1 is not a triangle according to a > b + c')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(2, 7, 3), 'NotATriangle', '2, 7, 3 is not a triangle according to b > a + c')

    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(3, 2, 9), 'NotATriangle', '3, 2, 9 is not a triangle according to c > a + b')

    def testMaxSidesTriangle(self):
        self.assertEqual(classifyTriangle(204, 2010, 201), 'InvalidInput', 'Checking for maximum boundary values')

    def testMinSidesTriangle(self):
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput', 'Checking for minimum boundary values')

    def testInvalidSidesTriangle(self):
        self.assertEqual(classifyTriangle('3', 2, 5), 'InvalidInput', 'Checking for invalid value types')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()