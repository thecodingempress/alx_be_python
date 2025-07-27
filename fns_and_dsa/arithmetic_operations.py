#function performs basic arithmetic operations

def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                raise ValueError("Cannot divide by zero.")
            elif num1 == 0:
                return 0
            return num1 / num2
        case _:
            raise ValueError("Invalid operation. Supported operations: add, subtract, multiply, divide.")

