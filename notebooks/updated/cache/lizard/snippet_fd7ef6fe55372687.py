def stelab(pobj, vobs):
    pobj = stypes.toDoubleVector(pobj)
    vobs = stypes.toDoubleVector(vobs)
    appobj = stypes.emptyDoubleVector(3)
    libspice.stelab_c(pobj, vobs, appobj)
    return stypes.cVectorToPython(appobj)