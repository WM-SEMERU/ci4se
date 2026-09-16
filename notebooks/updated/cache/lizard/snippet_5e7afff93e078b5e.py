def mle(D, tol=1e-07, method='meanprecision', maxiter=None):
    if method == 'meanprecision':
        return _meanprecision(D, tol=tol, maxiter=maxiter)
    else:
        return _fixedpoint(D, tol=tol, maxiter=maxiter)