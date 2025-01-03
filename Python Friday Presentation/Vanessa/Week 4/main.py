#Calculator Program
# n.b. The helper functions are in their own, separate file called 'math', for reusability
from math import add_numbers, subtract_numbers, multiply_numbers, divide_numbers
def calculator():
    #Displays a menu, takes user input, and calls the appropriate math functions.
    print("\nWelcome to Vanessa's Calculator Program!")
    while True:
    #a control flow statement that creates an infinite loop until user explicitly exits the program
        print("\nCalculator Menu:")
        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        try:
        #try/catch to handle all input cases, including outside of 1-5 and non-numbers
            #require value of input to be an integer
            choice = int(input("Choose an operation (1-5): "))
            if choice == 5:
                print("Thank you for using the calculator. Goodbye!")
                break
            #error handling number out of scope
            if choice not in [1, 2, 3, 4]:
                print("Invalid choice. Please select a whole number between 1 and 5.")
                continue
            #operation allows numerical input including floats
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            #assigning math functions for each menu option
            if choice == 1:
                print(f"Result: {add_numbers(num1, num2)}")
            elif choice == 2:
                print(f"Result: {subtract_numbers(num1, num2)}")
            elif choice == 3:
                print(f"Result: {multiply_numbers(num1, num2)}")
            elif choice == 4:
                print(f"Result: {divide_numbers(num1, num2)}")
        #error handling not an integer
        except ValueError:
            print("Invalid input. Please enter numerical values.")
        #default error handling for any other cases not handled above
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
# Main execution
if __name__ == "__main__":
    calculator()