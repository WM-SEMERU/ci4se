def saelgv(vec1, vec2):
    vec1 = stypes.toDoubleVector(vec1)
    vec2 = stypes.toDoubleVector(vec2)
    smajor = stypes.emptyDoubleVector(3)
    sminor = stypes.emptyDoubleVector(3)
    libspice.saelgv_c(vec1, vec2, smajor, sminor)
    return stypes.cVectorToPython(smajor), stypes.cVectorToPython(sminor)