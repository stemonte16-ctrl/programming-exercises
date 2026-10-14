"""Practice about classes"""

class Circle:
    """Represent a circle."""

    def __init__(self, radius):
        """Initialize a circle with a radius."""
        self.radius = radius



    def get_area(self):
        """Return the area of the circle."""
        area = 3.1416 * (self.radius ** 2)
        return area

#Create the first instance
circle = Circle(8)
print(circle.get_area())