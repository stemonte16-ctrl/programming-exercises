def contar_palabras():
    with open("07 manejo de archivos/texto23.txt", "r") as file:
        content = file.read()

    words = content.split()

    print("Este archivo contiene", len(words), "palabras")


contar_palabras()