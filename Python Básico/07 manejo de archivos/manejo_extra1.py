def unir_texto():
    with open("07 manejo de archivos/texto.txt", "r") as file:
        lines = file.readlines()

    text = ""

    for line in lines:
        text += line.strip() + " "

    with open("07 manejo de archivos/texto_unido.txt", "w") as file:
        file.write(text.strip())

    print("Archivo creado correctamente.")


unir_texto()