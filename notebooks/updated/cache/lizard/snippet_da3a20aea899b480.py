def bsrchc(value, ndim, lenvals, array):
    value = stypes.stringToCharP(value)
    ndim = ctypes.c_int(ndim)
    lenvals = ctypes.c_int(lenvals)
    array = stypes.listToCharArrayPtr(array, xLen=lenvals, yLen=ndim)
    return libspice.bsrchc_c(value, ndim, lenvals, array)