def pca(data=None, dim=-1, var_cutoff=0.95, stride=1, mean=None, skip=0,
    chunksize=None, **kwargs):
    r
    from pyemma.coordinates.transform.pca import PCA
    if mean is not None:
        import warnings
        warnings.warn('provided mean ignored', DeprecationWarning)
    res = PCA(dim=dim, var_cutoff=var_cutoff, mean=None, skip=skip, stride=
        stride)
    from pyemma.util.reflection import get_default_args
    cs = _check_old_chunksize_arg(chunksize, get_default_args(pca)[
        'chunksize'], **kwargs)
    if data is not None:
        res.estimate(data, chunksize=cs)
    else:
        res.chunksize = cs
    return res