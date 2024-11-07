# Andrew Deba
# UWYO COSC 1010
# 11/7/2024
# Lab 08
# Lab Section: 18
# Sources, people worked with, help given to: https://stackoverflow.com/questions/736043/checking-if-a-string-can-be-converted-to-float-in-python, 
# https://www.w3schools.com/python/ref_func_float.asp, https://www.w3schools.com/python/ref_math_sqrt.asp

# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def convert(string):
    if is_int(string) == True:
        return int(string)
    elif is_float(string) == True:
        return float(string)
    else:
        return False
def is_int_or_float(string):
    it_works = False
    for i in string:
        if i.isnumeric():
            continue
        if i != ".":
            return False
        if i == "." and it_works == True:
            return False
        if i == ".":
            it_works = True
    return True
def is_int(string):
    if is_int_or_float(string) == True:
        for i in string:
            if i == ".":
                return False
        return True
def is_float(string):
    if is_int_or_float(string) == True:
        for i in string:
            if i == ".":
                return True
        return False

string = input("Enter a string:")
final_val = convert(string)
print(type(final_val))

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def calculate_y_value(x,m,b,og_b,og_m):
    if if_negative(og_b):
        b = convert_negative(b)
    if if_negative(og_m):
        m = convert_negative(m)
    y = m*x + b
    return y

def if_negative_int(a):
    if a < 0:
        a = a*-1
        return a

def if_negative(a):
    if a[0] == "-":
        return True
    return False

def possible_neg_value(a):
    if if_negative(a) == True:
        a = a.replace("-","")    
    return a

def convert_negative(a):
    return (a*-1)

def yesno():
    if input("Would you like to enter another equation?").upper() == "YES":
        return True
    return False

while True:
    og_m = input("Enter a slope value:")
    m = convert(possible_neg_value(og_m))
    og_b = input("Enter a y intercept value:")
    b= convert(possible_neg_value(og_b))
    og_x1 = input("Enter a lower bound for the range of x:")
    x1 = convert(possible_neg_value(og_x1))
    og_x2 = input("Enter an upper bound for the range of x:")
    x2 = convert(possible_neg_value(og_x2))

    if if_negative(og_x1) == True:
        x = convert_negative(round(x1))
    else:
        x = round(x1)
    if if_negative(og_x2) == True:
        x2 = convert_negative(round(x2))
    else:
        x2 = round(x2)
    if x > x2:
        print("The lower bound of x must be less than the upper bound of x.")
        continue

    all_values_of_y = []

    while x <= x2:
        all_values_of_y.append(calculate_y_value(x,m,b,og_b,og_m))
        x += 1

    print(f"all possible values of y for your y=mx+b formula are {all_values_of_y}")
    if yesno() == True:
        continue
    break

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

import math

def square_root_of(a,b,c):
    b2 = b**2
    part2 = 4*a*c
    preFinal = b2 - part2
    if preFinal >= 0:
        final = math.sqrt(preFinal)
        return final
    return False

def caclulate_quadratic_equations_upper(a,b,c):
    x = 1
    final = []
    while x <= 2:
        if square_root_of(a,b,c) == False:
            return False
        neg_b = convert_negative(b)
        denom = 2*a
        if x == 1:
            numor = neg_b - square_root_of(a,b,c)
        if x == 2:
            numor = neg_b + square_root_of(a,b,c)
        final.append(numor/denom)
        x += 1
    return final

while True:
    og_a = input("Please enter a value for 'a' in the quadratic equation:")
    a = convert(possible_neg_value(og_a))
    if if_negative(og_a) == True:
        a = convert_negative(a)

    og_b = input("Please enter a value for 'b' in the quadratic equation:")
    b = convert(possible_neg_value(og_b))
    if if_negative(og_b) == True:
        b = convert_negative(b)

    og_c = input("Please enter a value for 'c' in the quadratic equation:")
    c = convert(possible_neg_value(og_c))
    if if_negative(og_c) == True:
        c = convert_negative(c)

    if caclulate_quadratic_equations_upper(a,b,c) == False:
        print("The values of x produced by the quadratic formula are non-existant")
    print(f"The values of x produced by the quadratic formula are {caclulate_quadratic_equations_upper(a,b,c)}")
    if yesno() == True:
        continue
    break