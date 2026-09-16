def _find_corresponding_multicol_key(key, keys_multicol):
    for mk in keys_multicol:
        if key.startswith(mk) and 'of' in key:
            return mk
    return None