def _dig(obj, *key):
    key = _splice_index(*key)
    if len(key) == 1:
        return obj[key[0]]
    return _dig(obj[key[0]], *key[1:])