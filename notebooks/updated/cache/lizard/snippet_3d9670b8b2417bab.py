def prior_rev(C, alpha=-1.0):
    r
    if isdense(C):
        return sparse.prior.prior_rev(C, alpha=alpha)
    else:
        warnings.warn('Prior will be a dense matrix for sparse input')
        return sparse.prior.prior_rev(C, alpha=alpha)