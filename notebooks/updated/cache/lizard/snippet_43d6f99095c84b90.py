def ilsr_rankings(n_items, data, alpha=0.0, initial_params=None, max_iter=
    100, tol=1e-08):
    fun = functools.partial(lsr_rankings, n_items=n_items, data=data, alpha
        =alpha)
    return _ilsr(fun, initial_params, max_iter, tol)