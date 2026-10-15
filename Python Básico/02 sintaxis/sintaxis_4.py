number_1 = int(input("Ingrese el primer numero: "))
number_2 = int(input("Ingrese el segundo numero: "))
number_3 = int(input("Ingrese el tercer numero: "))

if number_1 > number_2 and number_1 > number_3:
    print(f"El numero mayor es {number_1}")
elif number_2 > number_1 and number_2 > number_3:
    print(f"El numero mayor es {number_2}")
elif number_3 > number_1 and number_3 > number_2:
    print(f"El numero mayor es {number_3}")
else:
    print("Los tres numeros son iguales")