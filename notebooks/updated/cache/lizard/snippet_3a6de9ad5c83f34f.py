def prais(pmat):
    pmat = np.array(pmat)
    pr = 1 - np.diag(pmat)
    return pr