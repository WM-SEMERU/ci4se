def get_entry(key):
    if type(key) != str:
        raise TypeError('key must be str')
    if key not in _config:
        raise KeyError("Nonexistent entry '{key}'".format(key=key))
    return _config[key]