# static methods that calculates the square root value 
import math

class Calculator:
    
    @staticmethod
    def get_square_root(number):
        # Prevent math domain error for negative numbers
        if number < 0:
            return "Error: Cannot calculate square root of a negative number."
        return math.sqrt(number)

# Taking input from keyboard
try:
    num = float(input("Enter a number to find its square root: "))    
    result = Calculator.get_square_root(num)
    
    # Displaying the result
    if isinstance(result, str):
        print(result)
    else:
        print(f"The square root of {num} is: {result:.2f}")

except ValueError:
    print("Error: Please enter a valid numerical value.")