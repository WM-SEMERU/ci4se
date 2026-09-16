def lcase(instr, lenout=_default_len_out):
    instr = stypes.stringToCharP(instr)
    lenout = ctypes.c_int(lenout)
    outstr = stypes.stringToCharP(lenout)
    libspice.lcase_c(instr, lenout, outstr)
    return stypes.toPythonString(outstr)