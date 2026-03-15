"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""

def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and an operation (add, subtract, multiply, divide),
    then performs the operation on the two numbers and returns the result.

    Args:
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the operation.
    """

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")

def requestSanitizedNumber(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def requestSanitizedOperation(prompt: str) -> str:
    """Prompt the user until they enter a valid operation.

    Accepts: add, subtract, multiply, divide (case-insensitive).
    Returns the operation in lowercase.
    """
    valid_ops = {"add", "subtract", "multiply", "divide"}
    while True:
        op = input(prompt).strip().lower()
        if op in valid_ops:
            return op
        print("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")

def main():
    
    print(f"===== Simple Calculator =====")

    # Ask the user for sample input    
    num1 = requestSanitizedNumber("Enter the first number: ")
    num2 = requestSanitizedNumber("Enter the second number: ")
    operation = requestSanitizedOperation("Enter the operation (add, subtract, multiply, divide): ")

    # Perform the calculation and display the result
    result = simple_calculator(operation, num1, num2)
    verb_map = {
        "add": "adding",
        "subtract": "subtracting",
        "multiply": "multiplying",
        "divide": "dividing",
    }
    action = verb_map.get(operation, operation)
    print(f"The result of {action} {num1} and {num2} is: {result}")


if __name__ == "__main__":
    main()
