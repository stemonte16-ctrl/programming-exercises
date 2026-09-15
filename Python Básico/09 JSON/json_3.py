import json
import os


def load_pokemon(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)


def show_pokemon_by_type(pokemon_list, pokemon_type):
    found = False

    print("\nLos Pokémon que existen de ese tipo son:")

    for pokemon in pokemon_list:
        if pokemon["type"].lower() == pokemon_type.lower():
            print(pokemon["name"])
            found = True

    if not found:
        print("No se encontraron Pokémon de ese tipo.")


def main():
    folder = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(folder, "pokemon.json")

    pokemon_list = load_pokemon(file_name)

    pokemon_type = input("Ingrese el tipo de Pokémon que desea buscar: ")

    show_pokemon_by_type(pokemon_list, pokemon_type)


if __name__ == "__main__":
    main()