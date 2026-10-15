number_1 = int(input("Ingrese el primer numero: "))
number_2 = int(input("Ingrese el segundo numero: "))
number_3 = int(input("Ingrese el tercer numero: "))

added = number_1 + number_2 + number_3
if number_1 == 30 or number_2 == 30 or number_3 == 30:
    print("Correcto")
elif added == 30:
    print("correcto2")
else:
    print("Incorrecto")