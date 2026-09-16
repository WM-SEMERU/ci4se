def vamp_1_score(K, C00_train, C0t_train, Ctt_train, C00_test, C0t_test,
    Ctt_test, k=None):
    from pyemma._ext.variational.solvers.direct import spd_inv_sqrt
    U, S, V = _svd_sym_koopman(K, C00_train, Ctt_train)
    if k is not None:
        U = U[:, :k]
        V = V[:, :k]
    A = spd_inv_sqrt(mdot(U.T, C00_test, U))
    B = mdot(U.T, C0t_test, V)
    C = spd_inv_sqrt(mdot(V.T, Ctt_test, V))
    score = np.linalg.norm(mdot(A, B, C), ord='nuc')
    return score