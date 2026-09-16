def valid(names):
    if isinstance(names, str):
        names = [names]
        assert is_iterable_typed(names, basestring)
    return all(name in __all_features for name in names)