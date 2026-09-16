def from_dict(cls, d):
    key = d.get('name')
    options = d.get('options', None)
    subkey_list = d.get('subkeys', [])
    if len(subkey_list) > 0:
        subkeys = list(map(lambda k: AdfKey.from_dict(k), subkey_list))
    else:
        subkeys = None
    return cls(key, options, subkeys)