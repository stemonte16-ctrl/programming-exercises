def count_character(text, character):
    count = 0

    for letter in text:
        if letter == character:
            count += 1

    return count


text = "programacion"
character = input("Ingrese el carácter que desea buscar: ")

result = count_character(text, character)

print("Se ha encontrado", result, "veces el carácter")