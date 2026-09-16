def vsep(v1, v2):
    v1 = stypes.toDoubleVector(v1)
    v2 = stypes.toDoubleVector(v2)
    return libspice.vsep_c(v1, v2)