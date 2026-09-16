def dskv02(handle, dladsc, start, room):
    handle = ctypes.c_int(handle)
    start = ctypes.c_int(start)
    room = ctypes.c_int(room)
    n = ctypes.c_int()
    vrtces = stypes.emptyDoubleMatrix(3, room)
    libspice.dskv02_c(handle, dladsc, start, room, ctypes.byref(n), vrtces)
    return stypes.cMatrixToNumpy(vrtces)