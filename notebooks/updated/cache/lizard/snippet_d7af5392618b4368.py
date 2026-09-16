def __normalize_args(**keywds):
    if isinstance(keywds['name'], Callable) and None is keywds['function']:
        keywds['function'] = keywds['name']
        keywds['name'] = None
    return keywds