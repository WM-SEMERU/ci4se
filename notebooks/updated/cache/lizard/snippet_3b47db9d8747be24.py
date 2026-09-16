def dcyldr(x, y, z):
    x = ctypes.c_double(x)
    y = ctypes.c_double(y)
    z = ctypes.c_double(z)
    jacobi = stypes.emptyDoubleMatrix()
    libspice.dcyldr_c(x, y, z, jacobi)
    return stypes.cMatrixToNumpy(jacobi)