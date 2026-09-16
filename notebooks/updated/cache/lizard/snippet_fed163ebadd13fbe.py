def read_yaml(filename, add_constructor=None):
    y = read_file(filename)
    if add_constructor:
        if not isinstance(add_constructor, list):
            add_constructor = [add_constructor]
        for a in add_constructor:
            _yaml.add_constructor(*a)
    if y:
        return _yaml.load(y)