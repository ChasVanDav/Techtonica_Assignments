"""
Calculator Program
"""
def main():
    """
    Main function that serves as the entry point for the program.
    Displays a menu, takes user input, and calls the appropriate functions.
    """
    print("Welcome to the Basic Calculator!")
    while True:
        print("\nMenu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        try:
            choice = int(input("Choose an operation (1-5): "))

            if choice == 5:
                print("Thank you for using the calculator. Goodbye!")
                break

            if choice not in [1, 2, 3, 4]:
                print("Invalid choice. Please select a number between 1 and 5.")
                continue

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == 1:
                print(f"Result: {add_numbers(num1, num2)}")
            elif choice == 2:
                print(f"Result: {subtract_numbers(num1, num2)}")
            elif choice == 3:
                print(f"Result: {multiply_numbers(num1, num2)}")
            elif choice == 4:
                print(f"Result: {divide_numbers(num1, num2)}")

        except ValueError:
            print("Invalid input. Please enter numerical values.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

"""
Helper functions
"""
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


# Main execution
if __name__ == "__main__":
    main()