def image_file(path=None, zscript='self[1:]', xscript='[0,1]', yscript=
    'd[0]', g=None, **kwargs):
    if 'delimiter' in kwargs:
        delimiter = kwargs.pop('delimiter')
    else:
        delimiter = None
    d = _data.load(paths=path, delimiter=delimiter)
    if d is None or len(d) == 0:
        return
    default_kwargs = dict(xlabel=str(xscript), ylabel=str(yscript), title=d
        .path, clabel=str(zscript))
    default_kwargs.update(kwargs)
    X = d(xscript, g)
    Y = d(yscript, g)
    Z = _n.array(d(zscript, g))
    image_data(Z, X, Y, **default_kwargs)