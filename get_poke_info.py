import requests
import json
import pprint

"""
aims of exercise:
-return one pokemon dict from pokeapi
"""

def get_poke_info(pokemon_name):
    poke_url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name
    
    response = requests.get(url=poke_url)

    unfiltered_poke_dict = response.json()
    poke_dict = {}

    for key in unfiltered_poke_dict:
        if key in ["height", "name", "weight"]:
            poke_dict[key] = unfiltered_poke_dict[key]

        elif key == "moves":
            moves = []
            for move in unfiltered_poke_dict[key]:
                move_name = move["move"]["name"]
                moves.append(move_name)
            poke_dict[key] = moves

        elif key == "stats":
            stats = []
            for stat in unfiltered_poke_dict[key]:
                base_stat = stat["base_stat"]
                stat_name = stat["stat"]["name"]
                stats.append({stat_name: base_stat})
            poke_dict[key] = stats

        elif key == "types":
            types = []
            for type in unfiltered_poke_dict[key]:
                type_name = type["type"]["name"]
                types.append(type_name)
            poke_dict[key] = types

    return poke_dict

if __name__ == "__main__":
    p = pprint.PrettyPrinter(indent=4)
    p.pprint(get_poke_info("ditto"))
    p.pprint(get_poke_info("pikachu"))
    p.pprint(get_poke_info("articuno"))

# height ✅
# moves - list of dicts, with dict value containing "name" key we want the value of ✅
# name ✅
# stats - list of dicts, with "base_stat" containing an int, 
    # and "stat" cont a dict with a "name" key we want ✅
# type -  list of dicts, with "type" key cont another dict, with "name" key in it ✅
# weight ✅