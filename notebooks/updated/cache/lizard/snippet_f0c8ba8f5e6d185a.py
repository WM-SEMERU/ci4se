def max_variants(composition):
    max_n_variants = 0
    for element, count in composition.items():
        if element == 'H+':
            continue
        try:
            max_n_variants += count * periodic_table[element
                ].max_neutron_shift()
        except KeyError:
            pass
    return max_n_variants