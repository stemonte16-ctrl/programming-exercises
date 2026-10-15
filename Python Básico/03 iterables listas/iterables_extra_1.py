my_list = []

for i in range(7):
    number = int(input("Ingrese un número: "))
    my_list.append(number)

numero_a_buscar = int(input("Ingrese el número a buscar: "))

contador = 0

for number in my_list:
    if number == numero_a_buscar:
        contador += 1

print("El número", numero_a_buscar, "aparece", contador, "veces")