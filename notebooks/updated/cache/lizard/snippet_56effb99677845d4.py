def chebfun(f=None, domain=[-1, 1], N=None, chebcoeff=None):
    if chebcoeff is not None:
        return Chebfun.from_coeff(chebcoeff, domain)
    if isinstance(f, Polyfun):
        return Chebfun.from_fun(f)
    if hasattr(f, '__call__'):
        return Chebfun.from_function(f, domain, N)
    if np.isscalar(f):
        f = [f]
    try:
        iter(f)
    except TypeError:
        pass
    else:
        return Chebfun(f, domain)
    raise TypeError(
        'Impossible to initialise the object from an object of type {}'.
        format(type(f)))