"""
@author: vineet singh
This program implements the functionality to test if the triangle is Scalene, Isosceles, Equilateral or Right angled triangle
based on the given sides.
"""

import unittest

def classify_triangle(s1, s2, s3):
    """ this method takes 3 input parameters and return if it's Scalene, Isosceles, Equilateral or Right angled triangle  """

    # checks if side entered is above 0
    while s1 > 0 and s2 > 0 and s3 > 0:
        if s1 == s2 == s3:
            return 'Equilateral triangle'
        elif s1 == s2 or s2 == s3 or s3 == s1:
            return 'Isosceles triangle'
        elif s3*s3 == s1*s1 + s2*s2:
            return 'Right angled triangle'
        else:
            return 'Scalene triangle'
        break
    else:
        return 'Side cannot be negative or zero'

class UnitTests(unittest.TestCase):
    """ this class implements unit test cases """

    def test_classify_triangle_1(self):
        """ this method includes unit test to test classify_triangle for positive values """

        self.assertEqual(classify_triangle(5, 5, 5), 'Equilateral triangle')
        self.assertEqual(classify_triangle(7, 7, 3), 'Isosceles triangle')
        self.assertEqual(classify_triangle(3, 4, 5), 'Right angled triangle')
        self.assertEqual(classify_triangle(4, 6, 3), 'Scalene triangle')

    def test_classify_triangle_2(self):
        """ this method includes unit test to test classify_triangle for null values """

        self.assertEqual(classify_triangle(4, 6, 0), 'Side cannot be negative or zero')

    def test_classify_triangle_3(self):
        """ this method includes unit test to test classify_triangle for negative values """

        self.assertEqual(classify_triangle(4, 6, -5), 'Side cannot be negative or zero')

def main():
    """ this block controls the program flow """

    try:
        s1 = float(input('Enter side-1: '))
        s2 = float(input('Enter side-2: '))
        s3 = float(input('Enter side-3: '))

        res = classify_triangle(s1, s2, s3)
        if res != None: print(res)

    except ValueError:
        raise 'Please enter a valid value!'

if __name__ == '__main__':
    main()

# Unit Tests execution control
unittest.main(exit=False, verbosity=2)