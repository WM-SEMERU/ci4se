def rotmat(m1, angle, iaxis):
    m1 = stypes.toDoubleMatrix(m1)
    angle = ctypes.c_double(angle)
    iaxis = ctypes.c_int(iaxis)
    mout = stypes.emptyDoubleMatrix()
    libspice.rotmat_c(m1, angle, iaxis, mout)
    return stypes.cMatrixToNumpy(mout)