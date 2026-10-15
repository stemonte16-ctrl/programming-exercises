class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

class Inventory:
    def __init__(self):
        self.list_p = []
        
        
    def add_product(self,product):
        
        self.list_p.append(product)
        
    def show_products(self):
        
        for product in self.list_p:
            print()
            print(f"Nombre: {product.name}")
            print(f"Precio: {product.price}")
            print(f"Cantidad: {product.amount}")
    
    def calculate_value_invetory(self):
        sum_total = 0
        for product in self.list_p:
            total = product.price * product.amount
            sum_total = sum_total + total
        
        return sum_total

product1 = Product("Mouse",5000,3)
product2 = Product("Teclado", 8000, 2)

inventory = Inventory()
inventory.add_product(product1)
inventory.add_product(product2)
inventory.show_products()
print(inventory.calculate_value_invetory())