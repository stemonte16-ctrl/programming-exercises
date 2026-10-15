def get_name():
    name = input("Ingrese su nombre: ")

    if name.isdigit():
        raise ValueError("El nombre no puede ser un número")

    return name


def get_age():
    try:
        age = int(input("Ingrese su edad: "))
        return age
    except ValueError:
        print("Número no valido")
        return None


try:
    name = get_name()
    age = get_age()

    if age is not None:
        print("Hola", name + ",", "su edad es", age)

except ValueError as error:
    print(error)