def spkw20(handle, body, center, inframe, first, last, segid, intlen, n,
    polydg, cdata, dscale, tscale, initjd, initfr):
    handle = ctypes.c_int(handle)
    body = ctypes.c_int(body)
    center = ctypes.c_int(center)
    inframe = stypes.stringToCharP(inframe)
    first = ctypes.c_double(first)
    last = ctypes.c_double(last)
    segid = stypes.stringToCharP(segid)
    intlen = ctypes.c_double(intlen)
    n = ctypes.c_int(n)
    polydg = ctypes.c_int(polydg)
    cdata = stypes.toDoubleVector(cdata)
    dscale = ctypes.c_double(dscale)
    tscale = ctypes.c_double(tscale)
    initjd = ctypes.c_double(initjd)
    initfr = ctypes.c_double(initfr)
    libspice.spkw20_c(handle, body, center, inframe, first, last, segid,
        intlen, n, polydg, cdata, dscale, tscale, initjd, initfr)