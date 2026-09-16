def mtxvg(m1, v2, ncol1, nr1r2):
    m1 = stypes.toDoubleMatrix(m1)
    v2 = stypes.toDoubleVector(v2)
    ncol1 = ctypes.c_int(ncol1)
    nr1r2 = ctypes.c_int(nr1r2)
    vout = stypes.emptyDoubleVector(ncol1.value)
    libspice.mtxvg_c(m1, v2, ncol1, nr1r2, vout)
    return stypes.cVectorToPython(vout)