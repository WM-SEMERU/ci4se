def dict_of_numpyarray_to_dict_of_list(d):
    for key, value in d.iteritems():
        if isinstance(value, dict):
            d[key] = dict_of_numpyarray_to_dict_of_list(value)
        elif isinstance(value, np.ndarray):
            d[key] = value.tolist()
    return d