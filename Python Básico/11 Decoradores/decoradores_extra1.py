"""Extra exercise 1"""

def repeat_twice(function):
    """Decorator to repeat two times"""
    def wrapper(*args):
        result = function(*args)
        result_2 = function(*args)
        return result, result_2
    return wrapper


@repeat_twice
def show_name(name):
    """Function to show the name and greet"""
    print(f"Hola, {name}")

show_name("Steven")
