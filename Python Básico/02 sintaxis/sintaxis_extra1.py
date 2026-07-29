price = float(input("Ingrese el presio del articulo:"))

if price < 100 :
    discount = price * 0.02
else:
    discount = price * 0.1
final_price = price - discount
print(f"El precio final sería : {final_price}")