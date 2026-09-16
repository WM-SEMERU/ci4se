def ekacli(handle, segno, column, ivals, entszs, nlflgs, rcptrs, wkindx):
    handle = ctypes.c_int(handle)
    segno = ctypes.c_int(segno)
    column = stypes.stringToCharP(column)
    ivals = stypes.toIntVector(ivals)
    entszs = stypes.toIntVector(entszs)
    nlflgs = stypes.toIntVector(nlflgs)
    rcptrs = stypes.toIntVector(rcptrs)
    wkindx = stypes.toIntVector(wkindx)
    libspice.ekacli_c(handle, segno, column, ivals, entszs, nlflgs, rcptrs,
        wkindx)
    return stypes.cVectorToPython(wkindx)