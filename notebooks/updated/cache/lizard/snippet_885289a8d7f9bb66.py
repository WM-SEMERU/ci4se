def lstled(x, n, array):
    array = stypes.toDoubleVector(array)
    x = ctypes.c_double(x)
    n = ctypes.c_int(n)
    return libspice.lstled_c(x, n, array)