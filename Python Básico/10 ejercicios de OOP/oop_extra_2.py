"""abstract classes"""

from abc import ABC, abstractmethod

class User(ABC):
    """abstract parent class"""
    def __init__(self, name):
        """initialize the attributes"""
        self.name = name

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass

class AdminUser(User):
    def get_role(self):
        return "Admin"

    def has_permission(self, permission):
        return True

class RegularUser(User):
    def get_role(self):
        return "Regular"

    def has_permission(self, permission):
        permissions = ["read"]
        
        if permission in permissions:
            return True
        else:
            return False

user1 = AdminUser("Carlos")
user2 = RegularUser("Andrea")
print(user1.has_permission("delete"))  # True
print(user2.has_permission("delete"))  # False
