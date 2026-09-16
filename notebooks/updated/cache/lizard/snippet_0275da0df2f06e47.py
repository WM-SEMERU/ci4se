def rquad(a, b, c):
    a = ctypes.c_double(a)
    b = ctypes.c_double(b)
    c = ctypes.c_double(c)
    root1 = stypes.emptyDoubleVector(2)
    root2 = stypes.emptyDoubleVector(2)
    libspice.rquad_c(a, b, c, root1, root2)
    return stypes.cVectorToPython(root1), stypes.cVectorToPython(root2)