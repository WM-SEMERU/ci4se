def iterativeEMDS(X0, N, d, C, b, max_it=10, print_out=False, **kwargs):
    from pylocus.basics import mse, projection
    KE = kwargs.get('KE', None)
    KE_projected = KE.copy()
    d = len(X0)
    for i in range(max_it):
        KE_projected, cost, __ = projection(KE_projected, C, b)
        rank = np.linalg.matrix_rank(KE_projected)
        Xhat_KE, Vhat_KE = superMDS(X0, N, d, KE=KE_projected)
        KE_projected = Vhat_KE.dot(Vhat_KE.T)
        error = mse(C.dot(KE_projected), b)
        if print_out:
            print('cost={:2.2e},error={:2.2e}, rank={}'.format(cost, error,
                rank))
        if cost < 1e-20 and error < 1e-20 and rank == d:
            if print_out:
                print('converged after {} iterations'.format(i))
            return Xhat_KE, Vhat_KE
    print('iterativeMDS did not converge!')
    return None, None