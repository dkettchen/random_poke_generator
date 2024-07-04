import requests
from json import dump
import pprint


def get_pokedex():
    pokedex_url = 'https://pokeapi.co/api/v2/pokedex/1/'
    response = requests.get(url=pokedex_url)

    unfiltered_pokedex = response.json()
    pokemon = unfiltered_pokedex['pokemon_entries']
    poke_dict = {}
    for item in pokemon:
        poke_dict[item['entry_number']] = item['pokemon_species']['name']
    with open('pokedex.json', 'w', encoding='utf-8') as f:
        dump(poke_dict, f, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    get_pokedex()
