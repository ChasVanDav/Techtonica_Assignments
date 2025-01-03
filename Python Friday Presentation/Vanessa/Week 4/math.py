#Basic math functions defined here
#input/error handling in main file

#addition
def add_numbers(a, b):

    return a + b

#subtraction
def subtract_numbers(a, b):
    
    return a - b

#multiplication
def multiply_numbers(a, b):
    
    return a * b

#division
def divide_numbers(a, b):
   #check for zero division case which is undefinied
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

#to be imported into main file