"""Data validation"""

def decorate_function(function):
    """Decorate to data validate"""
    def wrapper(*args, **kwargs):

        for argument in args:
            if not isinstance(argument, (int, float)):
                raise TypeError("Numbers only")

        for value in kwargs.values():
            if not isinstance(value, (int, float)):
                raise TypeError()
        result = function(*args, **kwargs)
        return result
    return wrapper

@decorate_function
def calculate_total(a, b):
    """Function to test the decorator"""
    return a + b

print(calculate_total(10, 20))
calculate_total(10, "20")
