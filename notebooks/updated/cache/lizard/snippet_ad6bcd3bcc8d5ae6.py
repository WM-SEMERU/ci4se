def multi_find(*patterns, **kwargs):
    out = {}
    for pattern in set(patterns):
        search_result = find(pattern, best=kwargs.get('best', True),
            display=kwargs.get('display', _DEFAULT_DISPLAY))
        out[pattern] = search_result
    if not kwargs.get('display', _DEFAULT_DISPLAY):
        return out