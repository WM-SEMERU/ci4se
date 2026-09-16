def fn2lun(fname):
    fnameP = stypes.stringToCharP(fname)
    unit_out = ctypes.c_int()
    fname_len = ctypes.c_int(len(fname) + 1)
    libspice.fn2lun_(fnameP, ctypes.byref(unit_out), fname_len)
    return unit_out.value