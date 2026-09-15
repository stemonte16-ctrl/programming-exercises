import csv


def show_games(file_name):
    with open(file_name, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        next(reader)  # Saltar el encabezado

        for row in reader:
            print(f"Nombre: {row[0]}")
            print(f"Género: {row[1]}")
            print(f"Desarrollador: {row[2]}")
            print(f"Clasificación: {row[3]}")
            print()


def main():
    file_name = "videojuegos.csv"
    show_games(file_name)


if __name__ == "__main__":
    main()