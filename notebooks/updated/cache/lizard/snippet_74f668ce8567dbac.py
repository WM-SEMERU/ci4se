def sigFromPy(pobj):
    sig = getattr(pobj, 'dbusSignature', None)
    if sig is not None:
        return sig
    elif isinstance(pobj, int):
        return 'i'
    elif isinstance(pobj, six.integer_types):
        return 'x'
    elif isinstance(pobj, float):
        return 'd'
    elif isinstance(pobj, six.string_types):
        return 's'
    elif isinstance(pobj, list):
        vtype = type(pobj[0])
        same = True
        for v in pobj[1:]:
            if not vtype is type(v):
                same = False
        if same:
            return 'a' + sigFromPy(pobj[0])
        else:
            return 'av'
    elif isinstance(pobj, dict):
        same = True
        vtype = None
        for k, v in six.iteritems(pobj):
            if vtype is None:
                vtype = type(v)
            elif not vtype is type(v):
                same = False
        if same:
            return 'a{' + sigFromPy(k) + sigFromPy(v) + '}'
        else:
            return 'a{' + sigFromPy(k) + 'v}'
    else:
        raise MarshallingError('Invalid Python type for variant: ' + repr(pobj)
            )