def sort_func(kd1, kd2):
    _l = _cmp(kd1['type'], kd2['type'])
    if _l:
        return _l
    if kd1['type'] == 'EC':
        _l = _cmp(kd1['crv'], kd2['crv'])
        if _l:
            return _l
    _l = _cmp(kd1['type'], kd2['type'])
    if _l:
        return _l
    _l = _cmp(kd1['use'][0], kd2['use'][0])
    if _l:
        return _l
    try:
        _kid1 = kd1['kid']
    except KeyError:
        _kid1 = None
    try:
        _kid2 = kd2['kid']
    except KeyError:
        _kid2 = None
    if _kid1 and _kid2:
        return _cmp(_kid1, _kid2)
    elif _kid1:
        return -1
    elif _kid2:
        return 1
    return 0