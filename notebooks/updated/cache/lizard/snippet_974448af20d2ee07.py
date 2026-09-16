def uriencode(uristring, safe='', encoding='utf-8', errors='strict'):
    if not isinstance(uristring, bytes):
        uristring = uristring.encode(encoding, errors)
    if not isinstance(safe, bytes):
        safe = safe.encode('ascii')
    try:
        encoded = _encoded[safe]
    except KeyError:
        encoded = _encoded[b''][:]
        for i in _tointseq(safe):
            encoded[i] = _fromint(i)
        _encoded[safe] = encoded
    return b''.join(map(encoded.__getitem__, _tointseq(uristring)))