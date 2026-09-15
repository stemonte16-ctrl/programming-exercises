def convertir_a_entero(lista):
    for element in lista:
        try:
            number = int(element)
            print(element, "convertido a", number)

        except ValueError:
            print("No se pudo convertir el elemento:", element)


my_list = ["4", "hola", "10", "5.2"]

print("Resultado:")

convertir_a_entero(my_list)