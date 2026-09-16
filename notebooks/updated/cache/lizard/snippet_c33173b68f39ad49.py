def _set_default_key(mapping):
    key_longest = sorted([(len(v), k) for k, v in mapping.items()], reverse
        =True)[0][1]
    mapping['default'] = key_longest
    del mapping[key_longest]