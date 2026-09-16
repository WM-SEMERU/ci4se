def nvp2pl(normal, point):
    normal = stypes.toDoubleVector(normal)
    point = stypes.toDoubleVector(point)
    plane = stypes.Plane()
    libspice.nvp2pl_c(normal, point, ctypes.byref(plane))
    return plane