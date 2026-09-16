def ekopr(fname):
    fname = stypes.stringToCharP(fname)
    handle = ctypes.c_int()
    libspice.ekopr_c(fname, ctypes.byref(handle))
    return handle.value