def _add_atomic_percents_(elemental_array):
    n_atoms = _calculate_n_atoms_(elemental_array)
    for e in elemental_array:
        e['atomic_percent'] = e['occurances'] / n_atoms * 100
    return elemental_array