def to_astropy_column(llwcol, cls, copy=False, dtype=None, use_numpy_dtype=
    False, **kwargs):
    if dtype is None:
        dtype = _get_column_dtype(llwcol)
        if use_numpy_dtype and numpy.dtype(dtype).type is numpy.object_:
            try:
                dtype = NUMPY_TYPE_MAP[dtype]
            except KeyError:
                for key in NUMPY_TYPE_MAP:
                    if issubclass(dtype, key):
                        dtype = NUMPY_TYPE_MAP[key]
                        break
                else:
                    raise TypeError(
                        'no mapping from object type %r to numpy type' % dtype)
    try:
        return cls(data=llwcol, copy=copy, dtype=dtype, **kwargs)
    except TypeError:
        if dtype is numpy.int_ and isinstance(llwcol[0], ilwdchar_types):
            return cls(data=map(dtype, llwcol), copy=False, dtype=dtype, **
                kwargs)
        raise