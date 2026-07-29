message = "Hola desde la variable global"


def second_function():
    print("Esta es la segunda función")


def first_function():
    local_variable = "Soy una variable local"

    print("Esta es la primera función")
    second_function()

    print(local_variable)

    global message
    message = "La variable global fue modificada"


first_function()

print(message)