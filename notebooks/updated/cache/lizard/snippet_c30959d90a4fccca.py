def make_level_set(level):
    new_level = dict()
    for key, value in level.items():
        if isinstance(value, list):
            new_level[key] = set(value)
        else:
            new_level[key] = value
    return new_level