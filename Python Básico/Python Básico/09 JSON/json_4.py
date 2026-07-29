import json
import os


def load_pokemon(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)


def show_stats(pokemon_list):
    for pokemon in pokemon_list:
        print(f"Nombre: {pokemon['name']}")
        print(f"Ataque: {pokemon['attack']}")
        print(f"Defensa: {pokemon['defense']}")
        print(f"Velocidad: {pokemon['speed']}")
        print()


def main():
    folder = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(folder, "pokemon.json")

    pokemon_list = load_pokemon(file_name)

    show_stats(pokemon_list)


if __name__ == "__main__":
    main()