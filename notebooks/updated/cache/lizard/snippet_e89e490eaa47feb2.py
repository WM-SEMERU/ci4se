def cpos(string, chars, start):
    string = stypes.stringToCharP(string)
    chars = stypes.stringToCharP(chars)
    start = ctypes.c_int(start)
    return libspice.cpos_c(string, chars, start)