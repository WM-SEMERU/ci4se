def subpt(method, target, et, abcorr, obsrvr):
    method = stypes.stringToCharP(method)
    target = stypes.stringToCharP(target)
    abcorr = stypes.stringToCharP(abcorr)
    obsrvr = stypes.stringToCharP(obsrvr)
    spoint = stypes.emptyDoubleVector(3)
    alt = ctypes.c_double()
    if hasattr(et, '__iter__'):
        points = []
        alts = []
        for t in et:
            libspice.subpt_c(method, target, ctypes.c_double(t), abcorr,
                obsrvr, spoint, ctypes.byref(alt))
            checkForSpiceError(None)
            points.append(stypes.cVectorToPython(spoint))
            alts.append(alt.value)
        return points, alts
    else:
        et = ctypes.c_double(et)
        libspice.subpt_c(method, target, et, abcorr, obsrvr, spoint, ctypes
            .byref(alt))
        return stypes.cVectorToPython(spoint), alt.value