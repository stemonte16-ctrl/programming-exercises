"""Extra exercises 3"""
from datetime import date

def log_call(function):
    """Decorator to show info"""
    def wrapper(*args):
        result = function(*args)
        print(f"Func: {function.__name__} - args: {args}- date: {date.today()} Result: {result}")
        return result
    return wrapper

def validate_numbers(function):
    """Decorator to check the args"""
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("Only numbers")
        return function(*args)
    return wrapper

@log_call
@validate_numbers
def multiply(a, b):
    "Function to test both decorators"
    result = a * b
    return result

multiply("5", 3)
