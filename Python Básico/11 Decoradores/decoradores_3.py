"""Exercise 3 of decorators"""

class User:
    """Class user to test the decorator"""
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        """Property that returns the age"""
        return self.date_of_birth

user_1 = User(18)
user_2 = User(14)

def decorator_user(function):
    """Decorator to validate the age"""
    def wrapper(*args):
        if args[0].age < 18:
            raise ValueError("Minors not allowed")
        else:
            result = function(*args)
            print("Welcome")
        return result
    return wrapper

@decorator_user
def test_age(user):
    "Function to test the decorator"
    return user

test_age(user_1)
test_age(user_2)
