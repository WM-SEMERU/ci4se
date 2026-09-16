def wrap_penalty(p, fit_linear, linear_penalty=0.0):

    def wrapped_p(n, *args):
        if fit_linear:
            if n == 1:
                return sp.sparse.block_diag([linear_penalty], format='csc')
            return sp.sparse.block_diag([linear_penalty, p(n - 1, *args)],
                format='csc')
        else:
            return p(n, *args)
    return wrapped_p