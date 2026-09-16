def dskmi2(vrtces, plates, finscl, corscl, worksz, voxpsz, voxlsz, makvtl,
    spxisz):
    nv = ctypes.c_int(len(vrtces))
    vrtces = stypes.toDoubleMatrix(vrtces)
    np = ctypes.c_int(len(plates))
    plates = stypes.toIntMatrix(plates)
    finscl = ctypes.c_double(finscl)
    corscl = ctypes.c_int(corscl)
    worksz = ctypes.c_int(worksz)
    voxpsz = ctypes.c_int(voxpsz)
    voxlsz = ctypes.c_int(voxlsz)
    makvtl = ctypes.c_int(makvtl)
    spxisz = ctypes.c_int(spxisz)
    work = stypes.emptyIntMatrix(2, worksz)
    spaixd = stypes.emptyDoubleVector(10)
    spaixi = stypes.emptyIntVector(spxisz)
    libspice.dskmi2_c(nv, vrtces, np, plates, finscl, corscl, worksz,
        voxpsz, voxlsz, makvtl, spxisz, work, spaixd, spaixi)
    return stypes.cVectorToPython(spaixd), stypes.cVectorToPython(spaixi)