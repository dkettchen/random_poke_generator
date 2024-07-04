# random_poke_generator
Martin Colbourne (@FloatingBrioche) and I (Ren Zoller, @dkettchen) made some code to generate a random pokemon with a dictionary of info about it.

The returned dictionary is structured as follows:
{    'height': <height (int)>,
    'moves': [<moves (string)>],
    'name': <pokemon's name (string)>,
    'stats': [   {'hp': <hp (int)>},
                 {'attack': <attack (int)>},
                 {'defense': <defense (int)>},
                 {'special-attack': <special-attack (int)>},
                 {'special-defense': <special-defense (int)>},
                 {'speed': <speed (int)>}],
    'types': [<types (string)>],
    'weight': <weight (int)>}

If you need the pokedex entry number, you can find it as the key in the json pokedex.
