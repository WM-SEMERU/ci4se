def private_names_for(cls, names):
    if not isinstance(names, Iterable):
        raise TypeError('names must be an interable')
    return (private_name_for(item, cls) for item in names)