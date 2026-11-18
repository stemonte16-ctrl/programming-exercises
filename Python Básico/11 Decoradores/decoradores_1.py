"""Decorators"""

def decorator(function):
    """Function decorator"""
    def wrapper(*args, **kwargs):
        print("The best users")
        result = function(*args, **kwargs)
        print(*args)
        print(kwargs)
        return result
    return wrapper

@decorator
def users(user_1, user_2, user_3):
    """Decorated function"""
    return f"Welcome {user_1}, {user_2} and {user_3}"
print(users("Steven", "Nayu", user_3="Katherine"))
