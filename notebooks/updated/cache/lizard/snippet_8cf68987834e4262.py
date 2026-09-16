def _delete_keys(dct, keys):
    c = deepcopy(dct)
    assert isinstance(keys, list)
    for k in keys:
        c.pop(k)
    return c