def vprjpi(vin, projpl, invpl):
    vin = stypes.toDoubleVector(vin)
    vout = stypes.emptyDoubleVector(3)
    found = ctypes.c_int()
    libspice.vprjpi_c(vin, ctypes.byref(projpl), ctypes.byref(invpl), vout,
        ctypes.byref(found))
    return stypes.cVectorToPython(vout), bool(found.value)