import json
import os


def load_pokemon(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)


def show_pokemon(pokemon_list):
    for pokemon in pokemon_list:
        print(f"Nombre: {pokemon['name']}")
        print(f"Tipo: {pokemon['type']}")
        print(f"Habilidad: {pokemon['ability']}")
        print(f"HP: {pokemon['hp']}")
        print()


def main():
    folder = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(folder, "pokemon.json")

    pokemon_list = load_pokemon(file_name)

    show_pokemon(pokemon_list)


if __name__ == "__main__":
    main()