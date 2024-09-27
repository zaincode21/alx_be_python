
def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":  # Fix the typo
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:  # Handle division by zero
            return "Cannot divide by zero."
        return num1 / num2
