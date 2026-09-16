def check_species_object(species_name_or_object):
    if isinstance(species_name_or_object, Species):
        return species_name_or_object
    elif isinstance(species_name_or_object, str):
        return find_species_by_name(species_name_or_object)
    else:
        raise ValueError('Unexpected type for species: %s : %s' % (
            species_name_or_object, type(species_name_or_object)))