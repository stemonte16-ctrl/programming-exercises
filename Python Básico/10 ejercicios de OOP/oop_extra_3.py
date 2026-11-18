"""Encapsulation, Overriding"""

class Vehicle:
    """Parents class vehicle"""
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    def get_info(self):
        """Return the vehicle information"""
        return self._brand, self._year

class Car(Vehicle):
    """child class that receives vehicle"""
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self._doors = doors

    def get_info(self):
        return f"{self._brand} ({self._year}) - {self._doors} doors"

class Motorcycle(Vehicle):
    """child class that receives vehicle"""
    def __init__(self, brand, year, type_moto):
        super().__init__(brand, year)
        self._type = type_moto

    def get_info(self):
        return f"{self._brand} ({self._year}) - type: {self._type}"

vehicle1 = Car("Toyota", 2020, 4)
vehicle2 = Motorcycle("Yamaha", 2022, "Sports")


print(vehicle1.get_info())
print(vehicle2.get_info())
