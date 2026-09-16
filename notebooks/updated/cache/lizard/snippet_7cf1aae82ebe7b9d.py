def esrchc(value, array):
    value = stypes.stringToCharP(value)
    ndim = ctypes.c_int(len(array))
    lenvals = ctypes.c_int(len(max(array, key=len)) + 1)
    array = stypes.listToCharArray(array, xLen=lenvals, yLen=ndim)
    return libspice.esrchc_c(value, ndim, lenvals, array)