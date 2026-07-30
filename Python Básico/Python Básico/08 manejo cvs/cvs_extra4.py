import csv


def show_games_by_developer(file_name, developer_name):
    with open(file_name, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        next(reader)  # Saltar el encabezado

        found = False

        print(f"\nVideojuegos desarrollados por {developer_name}:")

        for row in reader:
            if row[2].lower() == developer_name.lower():
                print(f"- {row[0]} (Clasificación: {row[3]}, Género: {row[1]})")
                found = True

        if not found:
            print("No se encontraron videojuegos de ese desarrollador.")


def main():
    file_name = "videojuegos.csv"
    developer_name = input("Ingrese el nombre del desarrollador: ")

    show_games_by_developer(file_name, developer_name)


if __name__ == "__main__":
    main()