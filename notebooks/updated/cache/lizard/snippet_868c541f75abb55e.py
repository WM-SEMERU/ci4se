def pdinv(A, *args):
    L = jitchol(A, *args)
    logdet = 2.0 * np.sum(np.log(np.diag(L)))
    Li = dtrtri(L)
    Ai, _ = dpotri(L, lower=1)
    symmetrify(Ai)
    return Ai, L, Li, logdet