def dasac(handle, buffer):
    handle = ctypes.c_int(handle)
    n = ctypes.c_int(len(buffer))
    buflen = ctypes.c_int(max(len(s) for s in buffer) + 1)
    buffer = stypes.listToCharArrayPtr(buffer)
    libspice.dasac_c(handle, n, buflen, buffer)