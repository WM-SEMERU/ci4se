def mtxmg(m1, m2, ncol1, nr1r2, ncol2):
    m1 = stypes.toDoubleMatrix(m1)
    m2 = stypes.toDoubleMatrix(m2)
    mout = stypes.emptyDoubleMatrix(x=ncol2, y=ncol1)
    ncol1 = ctypes.c_int(ncol1)
    nr1r2 = ctypes.c_int(nr1r2)
    ncol2 = ctypes.c_int(ncol2)
    libspice.mtxmg_c(m1, m2, ncol1, nr1r2, ncol2, mout)
    return stypes.cMatrixToNumpy(mout)