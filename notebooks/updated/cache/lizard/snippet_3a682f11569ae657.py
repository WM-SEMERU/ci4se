def grad_eigh(ans, x, UPLO='L'):
    N = x.shape[-1]
    w, v = ans

    def vjp(g):
        wg, vg = g
        w_repeated = anp.repeat(w[..., anp.newaxis], N, axis=-1)
        off_diag = anp.ones((N, N)) - anp.eye(N)
        F = off_diag / (T(w_repeated) - w_repeated + anp.eye(N))
        return _dot(v * wg[(...), (anp.newaxis), :] + _dot(v, F * _dot(T(v),
            vg)), T(v))
    return vjp