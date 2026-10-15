def show_menu():
    print("\n1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Borrar resultado")
    print("6. Salir")


def get_number():
    try:
        number = float(input("Ingrese un número: "))
        return number
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        return None


def calculator():
    current_number = 0

    while True:
        print("\nNúmero actual:", current_number)

        show_menu()

        try:
            option = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: Debe ingresar una opción válida.")
            continue

        if option == 1:
            number = get_number()
            if number is not None:
                current_number += number

        elif option == 2:
            number = get_number()
            if number is not None:
                current_number -= number

        elif option == 3:
            number = get_number()
            if number is not None:
                current_number *= number

        elif option == 4:
            number = get_number()

            if number is not None:
                if number == 0:
                    print("Error: No se puede dividir entre cero.")
                else:
                    current_number /= number

        elif option == 5:
            current_number = 0
            print("Resultado borrado.")

        elif option == 6:
            print("Hasta luego.")
            break

        else:
            print("Error: Opción inválida.")


calculator()