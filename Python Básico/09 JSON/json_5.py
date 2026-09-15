import json
import os


def load_pokemon(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)


def show_average_level(pokemon_list):
    pokemon_types = {}

    for pokemon in pokemon_list:
        pokemon_type = pokemon["type"]
        level = pokemon["level"]

        if pokemon_type not in pokemon_types:
            pokemon_types[pokemon_type] = {
                "total_level": 0,
                "count": 0
            }

        pokemon_types[pokemon_type]["total_level"] += level
        pokemon_types[pokemon_type]["count"] += 1

    for pokemon_type in pokemon_types:
        average = (
            pokemon_types[pokemon_type]["total_level"]
            / pokemon_types[pokemon_type]["count"]
        )

        print(f"Tipo: {pokemon_type} → Promedio de nivel: {average:.1f}")


def main():
    folder = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(folder, "pokemon.json")

    pokemon_list = load_pokemon(file_name)

    show_average_level(pokemon_list)


if __name__ == "__main__":
    main()