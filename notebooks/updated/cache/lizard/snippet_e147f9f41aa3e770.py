def from_callback(cls, cb, nx=None, nparams=None, **kwargs):
    if kwargs.get('x_by_name', False):
        if 'names' not in kwargs:
            raise ValueError('Need ``names`` in kwargs.')
        if nx is None:
            nx = len(kwargs['names'])
        elif nx != len(kwargs['names']):
            raise ValueError(
                'Inconsistency between nx and length of ``names``.')
    if kwargs.get('par_by_name', False):
        if 'param_names' not in kwargs:
            raise ValueError('Need ``param_names`` in kwargs.')
        if nparams is None:
            nparams = len(kwargs['param_names'])
        elif nparams != len(kwargs['param_names']):
            raise ValueError(
                'Inconsistency between ``nparam`` and length of ``param_names``.'
                )
    if nparams is None:
        nparams = 0
    if nx is None:
        raise ValueError(
            'Need ``nx`` of ``names`` together with ``x_by_name==True``.')
    be = Backend(kwargs.pop('backend', None))
    x = be.real_symarray('x', nx)
    p = be.real_symarray('p', nparams)
    _x = dict(zip(kwargs['names'], x)) if kwargs.get('x_by_name', False) else x
    _p = dict(zip(kwargs['param_names'], p)) if kwargs.get('par_by_name', False
        ) else p
    try:
        exprs = cb(_x, _p, be)
    except TypeError:
        exprs = _ensure_3args(cb)(_x, _p, be)
    return cls(x, exprs, p, backend=be, **kwargs)