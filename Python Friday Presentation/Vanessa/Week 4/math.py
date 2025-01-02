def add_numbers(a, b):
    """
    Function to add two numbers.
    Parameters:
    a (float): First number
    b (float): Second number
    Returns:
    float: Sum of a and b
    """
    return a + b


def subtract_numbers(a, b):
    """
    Function to subtract two numbers.
    Parameters:
    a (float): First number
    b (float): Second number
    Returns:
    float: Difference of a and b
    """
    return a - b


def multiply_numbers(a, b):
    """
    Function to multiply two numbers.
    Parameters:
    a (float): First number
    b (float): Second number
    Returns:
    float: Product of a and b
    """
    return a * b


def divide_numbers(a, b):
    """
    Function to divide two numbers.
    Parameters:
    a (float): First number
    b (float): Second number
    Returns:
    float: Quotient of a and b
    Raises:
    ZeroDivisionError: If the second number (b) is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b
