#creating two basic functions (add_numbers, multiply_numbers) that take in numbers
#handling edge case of non-numbers using 'if not... or not' with 'isinstance' to test for wrong data type

def add_numbers(a, b):
    #if either of the inputs are not numbers (integers or floats) --> error message
    #otherwise execute calculations
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: Both inputs must be numbers"
    return a + b

def multiply_numbers(a, b):
    #if either of the inputs are not numbers (integers or floats) --> error message
    #otherwise execute calculations
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: Both inputs must be numbers"
    return a * b

# Modified function for deliberate testing failure
# def add_numbers(a, b):
#     #if either of the inputs are not numbers (integers or floats) --> error message
#     #otherwise execute calculations
#     if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
#         return "Error: Both inputs must be numbers"
#     return 10

#for additional evaluation criteria, please check presentation with screenshots starting at slide 7:
#https://docs.google.com/presentation/d/1jO0z5rszhrV0PcIKiPuVCbq70r4P4tHZBG6tlzV0VRk/edit#slide=id.p