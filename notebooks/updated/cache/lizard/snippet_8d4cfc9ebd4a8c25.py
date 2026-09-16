def extend_values(dictionary, key, items):
    values = dictionary.get(key, [])
    try:
        values.extend(items)
    except TypeError:
        raise TypeError('Expected a list, got: %r' % items)
    dictionary[key] = values