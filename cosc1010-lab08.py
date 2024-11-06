# Andrew Deba
# UWYO COSC 1010
# 11/7/2024
# Lab 08
# Lab Section: 18
# Sources, people worked with, help given to: https://stackoverflow.com/questions/736043/checking-if-a-string-can-be-converted-to-float-in-python, 
# https://www.w3schools.com/python/ref_func_float.asp

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
    for i in string:
        if i.isnumeric():
            continue
        if i != ".":
            return False
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

def calculate_y_value(x,m,b):
    if if_negative(x) == False and if_negative(m) == False and if_negative(b) == False:
        y = m*x + b
    if if_negative(x) == True and if_negative(m) == False and if_negative(b) == False:
        y = b - m*x
    if if_negative(x) == False and if_negative(m) == True and if_negative(b) == False:
        y = b - m*x
    if if_negative(x) == False and if_negative(m) == False and if_negative(b) == True:
        y = m*x - b
    if if_negative(x) == True and if_negative(m) == False and if_negative(b) == True:
        y = 0 - b - m*x
    if if_negative(x) == False and if_negative(m) == True and if_negative(b) == True:
        y = 0 - b - m*x
    return y
def if_negative_string(a):
    if a[0] == "-":
        return True
    return False
def possible_neg_value(a):
    if if_negative_string(a) == True:
        a = a.replace("-","")    
    return a
def if_negative(a):
    if a < 0:
        return True
    return False


m = convert(input("Enter a slope value:"))
b= convert(input("Enter a y intercept value:"))
x1 = convert(possible_neg_value(input("Enter a lower bound for the range of x:")))
x2 = convert(possible_neg_value(input("Enter an upper bound for the range of x:")))

all_values_of_y = []

if 



x = round(x1)
print(x1)

while x <= round(x2):
    all_values_of_y.append(calculate_y_value(x,m,b))
    x += 1

print(all_values_of_y)

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
