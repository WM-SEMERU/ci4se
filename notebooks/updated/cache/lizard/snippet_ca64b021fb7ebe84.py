def _encode_key(self, obj):
    if obj.__class__ is str:
        return self._encode_str(obj)
    if obj.__class__ is UUID:
        return '"' + str(obj) + '"'
    try:
        sx_encoder = obj.__mm_serialize__
    except AttributeError:
        pass
    else:
        try:
            data = sx_encoder()
        except NotImplementedError:
            pass
        else:
            return self._encode_key(data)
    if isinstance(obj, UUID):
        return '"' + str(obj) + '"'
    if isinstance(obj, str):
        return self._encode_str(obj)
    try:
        value = self.default(obj)
    except TypeError:
        raise TypeError('{!r} is not a valid dictionary key'.format(obj))
    return self._encode_key(value)