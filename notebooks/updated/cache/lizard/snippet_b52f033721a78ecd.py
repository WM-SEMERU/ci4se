def h5ftmp(**kwargs):
    suffix = kwargs.pop('suffix', '.h5')
    prefix = kwargs.pop('prefix', 'scikit_allel_')
    tempdir = kwargs.pop('dir', None)
    fn = tempfile.mktemp(suffix=suffix, prefix=prefix, dir=tempdir)
    atexit.register(os.remove, fn)
    kwargs['mode'] = 'w'
    h5f = h5py.File(fn, **kwargs)
    return h5f