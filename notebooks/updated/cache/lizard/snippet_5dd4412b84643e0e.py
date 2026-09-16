def _make_write_func(file_obj):
    if file_obj is None:
        return ffi.NULL

    @ffi.callback('cairo_write_func_t', error=constants.STATUS_WRITE_ERROR)
    def write_func(_closure, data, length):
        file_obj.write(ffi.buffer(data, length))
        return constants.STATUS_SUCCESS
    return write_func