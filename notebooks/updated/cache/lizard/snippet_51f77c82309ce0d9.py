def inrypl(vertex, direct, plane):
    assert isinstance(plane, stypes.Plane)
    vertex = stypes.toDoubleVector(vertex)
    direct = stypes.toDoubleVector(direct)
    nxpts = ctypes.c_int()
    xpt = stypes.emptyDoubleVector(3)
    libspice.inrypl_c(vertex, direct, ctypes.byref(plane), ctypes.byref(
        nxpts), xpt)
    return nxpts.value, stypes.cVectorToPython(xpt)