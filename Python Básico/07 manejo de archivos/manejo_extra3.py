def convertir_a_mayusculas(archivo_entrada, archivo_salida):
    with open(archivo_entrada, "r", encoding="utf-8") as entrada:
        with open(archivo_salida, "w", encoding="utf-8") as salida:
            for linea in entrada:
                salida.write(linea.upper())


def main():
    archivo_original = "archivo.txt"
    archivo_nuevo = "archivo_mayusculas.txt"

    convertir_a_mayusculas(archivo_original, archivo_nuevo)

    print("El archivo se convirtió a mayúsculas correctamente.")


if __name__ == "__main__":
    main()