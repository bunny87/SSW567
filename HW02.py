# -*- coding: utf-8 -*-
"""
Updated on Tuesday Februrary 5, 2018
The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: vineet singh

“I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment/examination. I further pledge that I have not copied
any material from a book, article, the Internet or any other source except where I
have expressly cited the source.”
"""

def classifyTriangle(a, b, c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    # updated position of isInstance block so as this block runs first to check if,
    # accepted type of value is provided, i.e. integer
    if not(isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    # updated condition "b <= b" to "b <= 0", as side should be checked against 0 not itself
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    # if (a > (b - c)) or (b > (c - a)) or (c > (a - b)):
    #     return 'NotATriangle'
    # updated first two conditions as per above comment for this block 
    if a > b + c or b > c + a or c > a + b:
        return 'NotATriangle'

    # now we know that we have a valid triangle
    # updated this condition to check if all three sides are equal to check if the triangle is equilateral
    if a == b == c:
        return 'Equilateral'

    # previously sides were multiplied by 2 which is not the condition,
    # correct condition is: (c * c) == (a ** a) + (b ** b)
    elif ((a ** 2) + (b ** 2)) == (c ** 2):
        return 'Right'

    # updated this condition so as to check if "a != c"
    elif (a != b) and  (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isoceles'