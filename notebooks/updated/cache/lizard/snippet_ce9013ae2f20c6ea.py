def get_string(cfunc, *args):
    cstr = get_ctype('const char**', cfunc, *args)
    return backend.ffi.string(cstr).decode() if cstr else None