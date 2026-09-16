def _AsList(arg):
    if isinstance(arg, string_types) or not isinstance(arg, collections.
        Iterable):
        return [arg]
    else:
        return list(arg)