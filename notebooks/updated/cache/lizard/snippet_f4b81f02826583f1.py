def gmres(A, b, x0=None, tol=1e-05, restrt=None, maxiter=None, xtype=None,
    M=None, callback=None, residuals=None, orthog='householder', **kwargs):
    if orthog == 'householder':
        x, flag = gmres_householder(A, b, x0=x0, tol=tol, restrt=restrt,
            maxiter=maxiter, xtype=xtype, M=M, callback=callback, residuals
            =residuals, **kwargs)
    elif orthog == 'mgs':
        x, flag = gmres_mgs(A, b, x0=x0, tol=tol, restrt=restrt, maxiter=
            maxiter, xtype=xtype, M=M, callback=callback, residuals=
            residuals, **kwargs)
    return x, flag