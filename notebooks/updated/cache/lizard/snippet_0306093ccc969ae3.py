def resistance(genename, resistance_dict):
    resistance_list = list()
    for resistance_class, gene_set in resistance_dict.items():
        if genename in gene_set:
            resistance_list.append(resistance_class)
    resistance = ','.join(sorted(resistance_list))
    return resistance