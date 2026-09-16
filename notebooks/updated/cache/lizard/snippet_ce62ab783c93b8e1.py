def trcnam(index, namlen=_default_len_out):
    index = ctypes.c_int(index)
    name = stypes.stringToCharP(namlen)
    namlen = ctypes.c_int(namlen)
    libspice.trcnam_c(index, namlen, name)
    return stypes.toPythonString(name)