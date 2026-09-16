def pddet(A):
    L = jitchol(A)
    logdetA = 2 * sum(np.log(np.diag(L)))
    return logdetA