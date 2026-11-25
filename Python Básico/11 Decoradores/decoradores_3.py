"""Exercise 3 of decorators"""
from datetime import date

class User:
    """Class user to test the decorator"""
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        """Property that returns the age"""
        today = date.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

user_1 = User(date(2000, 12, 20))
user_2 = User(date(2012, 5, 10))
print(user_1.age)
print(user_2.age)

def decorator_user(function):
    """Decorator to validate the age"""
    def wrapper(*args, **kwargs):
        user = args[0] if args else kwargs.get("user")
        
        if user.age < 18:
            raise ValueError("Minors not allowed")
        
        result = function(*args, **kwargs)
        print("Welcome")
        return result
    return wrapper

@decorator_user
def test_age(user):
    "Function to test the decorator"
    return user

test_age(user_1)
test_age(user=user_1)
#test_age(user_2)
