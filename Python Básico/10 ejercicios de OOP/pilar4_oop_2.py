"""Geometric shapes"""
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Class of geometric shapes"""

    @abstractmethod
    def calculate_perimeter(self):
        """Abstract method that represents the perimeter"""


    @abstractmethod
    def calculate_area(self):
        """Abstract method that represents the area"""

class Circle(Shape):
    """Class to work with the circle"""
    def __init__(self, radius):
        """initialize the parameters and attributes of circle"""
        self.radius = radius

    def calculate_perimeter(self):
        """Method to calculate the perimeter of circle"""
        return 2 * math.pi * self.radius

    def calculate_area(self):
        """Method to calculate the area of circle"""
        return math.pi * self.radius ** 2

class Square(Shape):
    """Class to work with the square"""
    def __init__(self, side):
        """Initialize the parameters and attributes of square"""
        self.side = side

    def calculate_perimeter(self):
        """Method to calculate the perimeter of square"""
        return 4 * self.side

    def calculate_area(self):
        """Method to calculate the area of square"""
        return self.side ** 2

class Rectangle(Shape):
    """Class to work with the rectangle"""
    def __init__(self, length, width):
        """Initialize the parameters and attributes of rectangle"""
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        """Method to calculate the perimeter of rectangle"""
        return 2 * (self.length + self.width)

    def calculate_area(self):
        """Method to calculate the area of rectangle"""
        return self.length * self.width

circle_1 = Circle(5)
print(f"The perimeter of circle is: {circle_1.calculate_perimeter()} ")
print(f"The area of circle is: {circle_1.calculate_area()} ")
print()
square_1 = Square(4)
print(f"The perimeter of square is: {square_1.calculate_perimeter()} ")
print(f"The area of square is: {square_1.calculate_area()} ")
print()
rectangle_1 = Rectangle(3, 6)
print(f"The perimeter of rectangle is: {rectangle_1.calculate_perimeter()} ")
print(f"The area of rectangle is: {rectangle_1.calculate_area()} ")
