def frmnam(frcode, lenout=_default_len_out):
    frcode = ctypes.c_int(frcode)
    lenout = ctypes.c_int(lenout)
    frname = stypes.stringToCharP(lenout)
    libspice.frmnam_c(frcode, lenout, frname)
    return stypes.toPythonString(frname)