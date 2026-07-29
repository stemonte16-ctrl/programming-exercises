def sumar_valores(lista):
    total = 0

    for element in lista:
        try:
            number = float(element)
            total += number

            print(number, "sumado correctamente")

        except ValueError:
            print("Elemento inválido:", element)

    print("Total de la suma:", total)


my_list = ["10", "manzana", "5.5", "3", "n/a"]

sumar_valores(my_list)