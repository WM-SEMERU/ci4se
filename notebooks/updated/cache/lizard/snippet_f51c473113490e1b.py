def loads(s, encoding=None, cls=JSONTreeDecoder, object_hook=None,
    parse_float=None, parse_int=None, parse_constant=None,
    object_pairs_hook=None, **kargs):
    return json.loads(s, encoding, cls, object_hook, parse_float, parse_int,
        parse_constant, object_pairs_hook, **kargs)