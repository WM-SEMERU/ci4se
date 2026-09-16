def make_symmetric(dict):
    for key, value in list(dict.items()):
        dict[value] = key
    return dict