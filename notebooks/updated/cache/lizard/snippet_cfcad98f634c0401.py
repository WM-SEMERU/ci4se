def subplots(scale_x=None, scale_y=None, scale=None, **kwargs):
    r
    if 'figsize' in kwargs:
        return plt.subplots(**kwargs)
    width, height = mpl.rcParams['figure.figsize']
    if scale is not None:
        width *= scale
        height *= scale
    if scale_x is not None:
        width *= scale_x
    if scale_y is not None:
        height *= scale_y
    nrows = kwargs.pop('nrows', 1)
    ncols = kwargs.pop('ncols', 1)
    width = ncols * width
    height = nrows * height
    return plt.subplots(nrows=nrows, ncols=ncols, figsize=(width, height),
        **kwargs)