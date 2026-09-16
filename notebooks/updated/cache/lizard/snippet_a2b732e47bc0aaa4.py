def apply_stat(f, arraylist, *extra, **kw):
    dtype = arraylist[0].dtype
    shape = arraylist[0].shape
    if dtype.names:
        new = numpy.zeros(shape, dtype)
        for name in dtype.names:
            new[name] = f([arr[name] for arr in arraylist], *extra, **kw)
        return new
    else:
        return f(arraylist, *extra, **kw)