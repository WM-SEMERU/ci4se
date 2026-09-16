def load_tempo(filename, delimiter='\\s+'):
    r
    t1, t2, weight = load_delimited(filename, [float, float, float], delimiter)
    weight = weight[0]
    tempi = np.concatenate([t1, t2])
    if len(t1) != 1:
        raise ValueError('Tempo file should contain only one line.')
    try:
        tempo.validate_tempi(tempi)
    except ValueError as error:
        warnings.warn(error.args[0])
    if not 0 <= weight <= 1:
        raise ValueError('Invalid weight: {}'.format(weight))
    return tempi, weight