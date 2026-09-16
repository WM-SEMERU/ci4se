def from_callback(cls, cb, ny=None, nparams=None, dep_transf_cbs=None,
    indep_transf_cbs=None, roots_cb=None, **kwargs):
    ny, nparams = _get_ny_nparams_from_kw(ny, nparams, kwargs)
    be = Backend(kwargs.pop('backend', None))
    x, = be.real_symarray('x', 1)
    y = be.real_symarray('y', ny)
    p = be.real_symarray('p', nparams)
    _y = dict(zip(kwargs['names'], y)) if kwargs.get('dep_by_name', False
        ) else y
    _p = dict(zip(kwargs['param_names'], p)) if kwargs.get('par_by_name', False
        ) else p
    exprs = _ensure_4args(cb)(x, _y, _p, be)
    if dep_transf_cbs is not None:
        dep_transf = [(fw(yi), bw(yi)) for (fw, bw), yi in zip(
            dep_transf_cbs, y)]
    else:
        dep_transf = None
    if indep_transf_cbs is not None:
        indep_transf = indep_transf_cbs[0](x), indep_transf_cbs[1](x)
    else:
        indep_transf = None
    if kwargs.get('dep_by_name', False):
        exprs = [exprs[k] for k in kwargs['names']]
    cls._kwargs_roots_from_roots_cb(roots_cb, kwargs, x, _y, _p, be)
    return cls(list(zip(y, exprs)), x, dep_transf, indep_transf, p, backend
        =be, **kwargs)