def BVV(value, size=None, **kwargs):
    if type(value) in (bytes, str):
        if type(value) is str:
            l.warning('BVV value is a unicode string, encoding as utf-8')
            value = value.encode('utf-8')
        if size is None:
            size = len(value) * 8
        elif type(size) is not int:
            raise TypeError(
                'Bitvector size  must be either absent (implicit) or an integer'
                )
        elif size != len(value) * 8:
            raise ClaripyValueError('string/size mismatch for BVV creation')
        value = int(binascii.hexlify(value), 16) if value != b'' else 0
    elif size is None or type(value) is not int and value is not None:
        raise TypeError(
            'BVV() takes either an integer value and a size or a string of bytes'
            )
    if value is not None:
        value &= (1 << size) - 1
    if not kwargs:
        try:
            return _bvv_cache[value, size]
        except KeyError:
            pass
    result = BV('BVV', (value, size), length=size, **kwargs)
    _bvv_cache[value, size] = result
    return result