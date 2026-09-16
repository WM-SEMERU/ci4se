def twovec(axdef, indexa, plndef, indexp):
    axdef = stypes.toDoubleVector(axdef)
    indexa = ctypes.c_int(indexa)
    plndef = stypes.toDoubleVector(plndef)
    indexp = ctypes.c_int(indexp)
    mout = stypes.emptyDoubleMatrix()
    libspice.twovec_c(axdef, indexa, plndef, indexp, mout)
    return stypes.cMatrixToNumpy(mout)