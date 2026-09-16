def fft_propagate(fftfield, d, nm, res, method='helmholtz', ret_fft=False):
    fshape = len(fftfield.shape)
    assert fshape in [1, 2], 'Dimension of `fftfield` must be 1 or 2.'
    if fshape == 1:
        func = fft_propagate_2d
    else:
        func = fft_propagate_3d
    names = func.__code__.co_varnames[:func.__code__.co_argcount]
    loc = locals()
    vardict = dict()
    for name in names:
        vardict[name] = loc[name]
    return func(**vardict)