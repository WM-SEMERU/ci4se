def _get_epoch(_str):
    _return = None
    if _str.startswith('A.D. '):
        _return = 'ad'
    elif _str.startswith('a. A.D. '):
        _return = None
    elif _str.startswith('p. A.D. '):
        _return = 'ad'
    elif regex.match('^[0-9]+ B\\.C\\. *', _str):
        _return = 'bc'
    elif regex.match('^a\\. *[0-9]+ B\\.C\\. *', _str):
        _return = 'bc'
    elif regex.match('^p\\. *[0-9]+ B\\.C\\. *', _str):
        _return = None
    elif _str == 'Incertum' or _str == 'Varia':
        _return = _str
    return _return