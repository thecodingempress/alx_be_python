

from unittest import case


def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling division by zero.
    """

    try:
        if not isinstance(numerator, (int, float)):
            numerator = float(numerator)

        if not isinstance(denominator, (int, float)):
            denominator = float(denominator)

        result = numerator / denominator
    
    except ZeroDivisionError:
        return("Error: Cannot divide by zero.")
    
    except ValueError:
        return("Error: Please enter numeric values only.")
    
    else:
        return f"The result of the division is {result}"