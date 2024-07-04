from get_poke_info import get_poke_info
from json import loads
import pprint
from random import randint

def get_random_poke():
    with open("pokedex.json", "r", encoding="utf-8") as pokedex:
        read_data = pokedex.read()
        pokedex_dict = loads(read_data)
    numerical_pokedex = {int(key): pokedex_dict[key] for key in pokedex_dict}

    number = randint(1, 1025)
    pokemon_name = numerical_pokedex[number]
    return get_poke_info(pokemon_name)


if __name__ == "__main__":
    p = pprint.PrettyPrinter(indent=4)
    p.pprint(get_random_poke())