import csv


def show_games_by_rating(file_name, rating):
    with open(file_name, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        next(reader)  # Saltar el encabezado

        found = False

        for row in reader:
            if row[3].upper() == rating.upper():
                print(f"Nombre: {row[0]}")
                print(f"Género: {row[1]}")
                print(f"Desarrollador: {row[2]}")
                print(f"Clasificación: {row[3]}")
                print()

                found = True

        if not found:
            print("No se encontraron videojuegos con esa clasificación.")


def main():
    file_name = "videojuegos.csv"
    rating = input("Ingrese una clasificación ESRB: ")

    show_games_by_rating(file_name, rating)


if __name__ == "__main__":
    main()