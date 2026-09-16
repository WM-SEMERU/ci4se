def diags2(symmat):
    symmat = stypes.toDoubleMatrix(symmat)
    diag = stypes.emptyDoubleMatrix(x=2, y=2)
    rotateout = stypes.emptyDoubleMatrix(x=2, y=2)
    libspice.diags2_c(symmat, diag, rotateout)
    return stypes.cMatrixToNumpy(diag), stypes.cMatrixToNumpy(rotateout)