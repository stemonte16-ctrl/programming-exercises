import json
import os


def load_pokemon(file_name):
    if not os.path.exists(file_name):
        return []

    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)


def get_new_pokemon():
    name = input("Ingrese el nombre del Pokémon: ")
    pokemon_type = input("Ingrese el tipo del Pokémon: ")
    ability = input("Ingrese la habilidad: ")
    hp = int(input("Ingrese los puntos de vida (HP): "))

    return {
        "name": name,
        "type": pokemon_type,
        "ability": ability,
        "hp": hp
    }


def save_pokemon(file_name, pokemon_list):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(pokemon_list, file, indent=4)


def main():
    folder = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(folder, "pokemon.json")

    pokemon_list = load_pokemon(file_name)

    new_pokemon = get_new_pokemon()

    pokemon_list.append(new_pokemon)

    save_pokemon(file_name, pokemon_list)

    print("El Pokémon se agregó correctamente.")


if __name__ == "__main__":
    main()