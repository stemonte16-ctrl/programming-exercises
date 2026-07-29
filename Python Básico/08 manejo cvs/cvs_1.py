import csv


def solicitar_videojuego():
    nombre = input("Ingrese el nombre del videojuego: ")
    genero = input("Ingrese el género: ")
    desarrollador = input("Ingrese el desarrollador: ")
    clasificacion = input("Ingrese la clasificación ESRB: ")

    return [nombre, genero, desarrollador, clasificacion]


def guardar_videojuegos(nombre_archivo, cantidad):
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)

        escritor.writerow(["nombre", "genero", "desarrollador", "clasificacion"])

        for i in range(cantidad):
            print(f"\nVideojuego #{i + 1}")
            videojuego = solicitar_videojuego()
            escritor.writerow(videojuego)


def main():
    cantidad = int(input("¿Cuántos videojuegos desea ingresar? "))
    nombre_archivo = "videojuegos.csv"

    guardar_videojuegos(nombre_archivo, cantidad)

    print("\nLos videojuegos se guardaron correctamente en videojuegos.csv")


if __name__ == "__main__":
    main()