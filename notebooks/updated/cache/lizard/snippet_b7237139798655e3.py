def lookup_pokemon(field, value, pokemons=None):
    if pokemons == None:
        pokemons = catch_em_all()
    catches = {}
    for pid, data in pokemons.items():
        if isinstance(data[field], list):
            for entry in data[field]:
                found = search_entry(entry, value)
                if found == True:
                    catches[pid] = data
        else:
            found = search_entry(data[field], value)
            if found == True:
                catches[pid] = data
    if len(catches) > 0:
        return catches
    return None