"""Ejercicio extra de OOP"""

class Rectangle:
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Existe un valor negativo, los valores deben ser positivos")
        
        self.width = width
        self.height = height
        
    def get_area(self):
        
        area = self.width * self.height
        return area
        
    def get_perimeter(self):
        
        perimeter = 2 * (self.width + self.height)
        return perimeter
        

while True:
    width_1 = int(input("Ingrese el ancho del rectangulo:"))
    height_1 = int(input("Ingrese el largo del rectangulo: "))
    try:
        if width_1 < 0 or height_1 < 0:
            raise ValueError()
        break
    except ValueError:
        print("Existe un valor negativo, los valores deben ser positivos")



rectangle = Rectangle(width_1, height_1)
print(f"El area del rectangulo es: {rectangle.get_area()}")
print(f"El perimetro del rectangulo es: {rectangle.get_perimeter()}")