def mutable_record_transform(cls):
    if not (len(cls.bases) > 0 and isinstance(cls.bases[0], astroid.Call) and
        cls.bases[0].func.as_string() == 'mutablerecords.Record'):
        return
    try:
        if len(cls.bases[0].args) >= 2:
            for a in cls.bases[0].args[1].elts:
                cls.locals[a] = [None]
        if len(cls.bases[0].args) >= 3:
            for a, b in cls.bases[0].args[2].items:
                cls.locals[a.value] = [None]
    except:
        raise SyntaxError('Invalid mutablerecords syntax')