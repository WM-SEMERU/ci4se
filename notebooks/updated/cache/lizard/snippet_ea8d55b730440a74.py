def set_dict_value(dictionary, keys, value):
    orig = dictionary
    for key in keys[:-1]:
        dictionary = dictionary.setdefault(key, {})
    dictionary[keys[-1]] = value
    return orig