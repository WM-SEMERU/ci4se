def _ctypes_dtype(parameter):
    ctype = parameter.ctype
    if ctype is None:
        if parameter.kind is not None:
            return '{}({})'.format(parameter.dtype, parameter.kind)
        else:
            return parameter.dtype
    else:
        return '{}({})'.format(parameter.dtype, ctype)