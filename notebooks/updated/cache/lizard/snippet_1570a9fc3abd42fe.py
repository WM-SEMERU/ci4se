def system_repertoire_distance(r1, r2):
    if config.MEASURE in measures.asymmetric():
        raise ValueError(
            '{} is asymmetric and cannot be used as a system-level irreducibility measure.'
            .format(config.MEASURE))
    return measures[config.MEASURE](r1, r2)