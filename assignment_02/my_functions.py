# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Name: Brandon Juffe 
#
# Date: 1/28/2020
# 
##################################################
#
# Sample Script for Assignment 2: 
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

# import name_of_module

# import math 
    # For excercise 2, 3 & 5


##################################################
# Function Definitions
##################################################

# Exercise 1

def average(num1: float, num2: float) -> float:
    """Return the average of num1 and num2.
    >>> average(10,20)
    15.0
    >>> average(2.5, 3.0)
    2.75
    >>> average(4.7, 8.3)
    6.5
    """

    return (num1 + num2) / 2

# Exercise 2

import math 

def area_of_circle(r):
    """Return area of circle from variable r 
    >>> area_of_circle(6)
    113.097
    >>> area_of_circle(15)
    706.858
    >>> area_of_circle(2.5)
    19.635
    """
    
    return (r**2 * math.pi)

# Exercise 3

import math

def volume_of_cylinder(r,h):
    """Return Volume of Cylinder using r and h 
    >>> volume_of_cylinder(6,4)
    452.389
    >>> volume_of_cylinder(3,7)
    197.920
    >>> volume_of_cylinder(2,9)
    113.097
    """
    
    return ((math.pi) * (r**2)* (h))

# Exercise 4

def utility(x, y, alpha):
    """Return Value of Cobb-Douglass Utility Function
    >>> utility(5,6,.05)
    5.946
    >>> utility(7,4,.1)
    4.230
    >>> utility(8.3,13,.01)
    12.942
    """
    
    return (x**alpha) * (y**(1-alpha))


# Exercise 5

import math

def logit(x, B0, B1):
    """Return Value of the Value of the Logit Link Function 
    >>> logit(3, 18, 12)
    2.8307533032746943e+23
    >>> logit(5, 12, 7)
    1.1420073898156839e+26
    >>> logit(7, 10, 7)
    2.5154386709191646e+30
    """
    
    return (math.exp(x)**B0+(x*B1)) % (math.exp(x)**(B0+(x*B1)) + 1)

print('#' + 50*"-")
print('#' + 50*"-")
print("Testing my Examples for Excercise 1")

print('#' + 50*"-")
print("Exercise 1, Example 1:")
print("Evaluating average(10,20)")
print("Expected: " + str(15.0))
print("Got: " + str(average(10,20)))    


print("#" + 50*"-")
print("Exercise 1, Example 2:")
print("Evaluating average(2.5, 3.0)")
print("Expected: " + str(2.75))
print("Got: " + str(average(2.5, 3.0)))


print("#" + 50*"-")
print("Exercise 1, Example 3:")
print("Evaluating average(4.7, 8.3)")
print("Expected: " + str(6.5))
print("Got: " + str(average(4.7,8.3)))


print('#' + 50*"-")
print("Testing my Examples for Excercise 2")


print('#' + 50*"-")
print('Excercise 2, Example 1:')
print("Evaluating area_of_circle(6)")
print("Expected: " + str(113.097))
print("Got: " + str(area_of_circle(6)))


print('#' + 50*"-")
print('Excercise 2, Example 2:')
print("Evaluating area_of_circle(15)")
print("Expected: " + str(706.858))
print("Got: " + str(area_of_circle(15)))


print('#' + 50*"-")
print('Excercise 2, Example 3:')
print("Evaluating area_of_circle(2.5)")
print("Expected: " + str(19.635))
print("Got: " + str(area_of_circle(2.5)))


print('#' + 50*"-")
print("Testing my Examples for Excercise 3")


print('#' + 50*"-")
print('Excercise 3, Example 1:')
print("Evaluating volume_of_cylinder(6,4)")
print("Expected: " + str(452.389))
print("Got: " + str(volume_of_cylinder(6,4)))


print('#' + 50*"-")
print('Excercise 3, Example 2:')
print("Evaluating volume_of_cylinder(3,7)")
print("Expected: " + str(197.920))
print("Got: " + str(volume_of_cylinder(3,7)))


print('#' + 50*"-")
print('Excercise 3, Example 3:')
print("Evaluating volume_of_cylinder(2,9)")
print("Expected: " + str(113.097))
print("Got: " + str(volume_of_cylinder(2,9)))


print('#' + 50*"-")
print("Testing my Examples for Excercise 4")


print('#' + 50*"-")
print('Excercise 4, Example 1:')
print("Evaluating utility(5,6,.05)")
print("Expected: " + str(5.946))
print("Got: " + str(utility(5, 6,.05)))


print('#' + 50*"-")
print('Excercise 4, Example 2:')
print("Evaluating utility(7,4,.1)")
print("Expected: " + str(4.230))
print("Got: " + str(utility(7,4,.1)))


print('#' + 50*"-")
print('Excercise 4, Example 3:')
print("Evaluating utility(8.3,13,.01)")
print("Expected: " + str(12.941))
print("Got: " + str(utility(8.3,13,.01)))


print('#' + 50*"-")
print("Testing my Examples for Excercise 4")


print('#' + 50*"-")
print('Excercise 5, Example 1:')
print("Evaluating logit(3,18,12)")
print("Expected: " + str(2.8307533032746943e+23))
print("Got: " + str(logit(3,18,12)))


print('#' + 50*"-")
print('Excercise 5, Example 2:')
print("Evaluating logit(5,12,7)")
print("Expected: " + str(1.1420073898156839e+26))
print("Got: " + str(logit(5,12,7)))


print('#' + 50*"-")
print('Excercise 5, Example 3:')
print("Evaluating logit(7,10,7)")
print("Expected: " + str(2.5154386709191646e+30))
print("Got: " + str(logit(7,10,7)))


##################################################
# End
##################################################