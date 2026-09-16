def reclat(rectan):
    rectan = stypes.toDoubleVector(rectan)
    radius = ctypes.c_double(0)
    longitude = ctypes.c_double(0)
    latitude = ctypes.c_double(0)
    libspice.reclat_c(rectan, ctypes.byref(radius), ctypes.byref(longitude),
        ctypes.byref(latitude))
    return radius.value, longitude.value, latitude.value