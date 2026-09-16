def glBufferData(target, data, usage):
    if isinstance(data, int):
        size = data
        data = ctypes.c_voidp(0)
    else:
        if not data.flags['C_CONTIGUOUS'] or not data.flags['ALIGNED']:
            data = data.copy('C')
        data_ = data
        size = data_.nbytes
        data = data_.ctypes.data
    try:
        nativefunc = glBufferData._native
    except AttributeError:
        nativefunc = glBufferData._native = _get_gl_func('glBufferData',
            None, (ctypes.c_uint, ctypes.c_int, ctypes.c_void_p, ctypes.c_uint)
            )
    res = nativefunc(target, size, data, usage)