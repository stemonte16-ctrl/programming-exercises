import csv


def count_genres(file_name):
    genres = {}

    with open(file_name, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        next(reader)  # Saltar el encabezado

        for row in reader:
            genre = row[1]

            if genre in genres:
                genres[genre] += 1
            else:
                genres[genre] = 1

    return genres


def show_genres(genres):
    print("Géneros encontrados:")

    for genre in sorted(genres):
        print(f"{genre}: {genres[genre]}")


def main():
    file_name = "videojuegos.csv"

    genres = count_genres(file_name)
    show_genres(genres)


if __name__ == "__main__":
    main()