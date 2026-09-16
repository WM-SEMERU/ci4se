def values_to_array(input_values):
    if type(input_values) == tuple:
        values = np.array(input_values).reshape(-1, 1)
    elif type(input_values) == np.ndarray:
        values = np.atleast_2d(input_values)
    elif type(input_values) == int or type(input_values) == float or type(np
        .int64):
        values = np.atleast_2d(np.array(input_values))
    else:
        print('Type to transform not recognized')
    return values