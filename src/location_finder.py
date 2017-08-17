import operator
locations_path = '../resources/locations.txt'
uncaptured_pokes_path = '../resources/uncaptured_pokes.txt'
result_path = '../resources/result_locations.txt'

def extract_pokeinfo():
    """ Returns a dict mapping the pokemon id to its capture location. """
    poke_locations = dict()
    poke_names = dict()
    with open(locations_path, 'r') as pokes:
        for poke in pokes:
            poke_info = list(filter(None, poke.split('\t')))
            poke_id = int(poke_info[0][2:])
            poke_name = poke_info[1]
            poke_location = poke_info[-1].rstrip('\n')

            poke_locations[poke_id] = poke_location
            poke_names[poke_id] = poke_name
    return poke_locations, poke_names


def get_pokeids():
    """ Returns all the ids of pokemons not yet captured. """
    with open(uncaptured_pokes_path, 'r') as f:
        return [int(line.rstrip('\n')) for line in f.readlines()]


def get_entries(poke_ids, poke_locations):
    """ Returns entries sorted by location. """
    result = dict()
    for poke_id in poke_ids:
        result[poke_id] = poke_locations[poke_id]
    return result


def get_grouped_locations(poke_locs, poke_names):
    pokes = sorted(poke_locs.items(), key=operator.itemgetter(1))
    entries = []
    for poke in pokes:
        poke_info = '%3d: %10s - %s' % (poke[0], poke_names[poke[0]], poke[1])
        entries.append(poke_info)
    return entries

def save_locations(poke_locs):
    file = open(result_path, 'w')
    for poke_loc in poke_locs:
        file.write('%s\n' % poke_loc)
    file.close()


if __name__ == '__main__':
    poke_locs, poke_names = extract_pokeinfo()
    ids = get_pokeids()
    uncaptured_pokemon_locs = get_entries(ids, poke_locs)
    sorted_locs = get_grouped_locations(uncaptured_pokemon_locs, poke_names)

    # Print all the pokemon capture locations to the console
    for loc in sorted_locs:
        print(loc)

    # Save all the pokemon capture locations to the result_locations.txt file
    save_locations(sorted_locs)