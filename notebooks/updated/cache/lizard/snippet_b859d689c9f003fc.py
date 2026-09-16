def mtxv(m1, vin):
    m1 = stypes.toDoubleMatrix(m1)
    vin = stypes.toDoubleVector(vin)
    vout = stypes.emptyDoubleVector(3)
    libspice.mtxv_c(m1, vin, vout)
    return stypes.cVectorToPython(vout)