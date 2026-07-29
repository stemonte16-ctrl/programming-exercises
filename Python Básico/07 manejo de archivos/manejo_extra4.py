def agregar_texto(nombre_archivo, texto):
    with open(nombre_archivo, "a", encoding="utf-8") as archivo:
        archivo.write(texto + "\n")


def main():
    nombre_archivo = "registros.txt"
    texto = input("Ingrese una línea de texto: ")

    agregar_texto(nombre_archivo, texto)

    print("El texto se agregó al final del archivo.")


if __name__ == "__main__":
    main()