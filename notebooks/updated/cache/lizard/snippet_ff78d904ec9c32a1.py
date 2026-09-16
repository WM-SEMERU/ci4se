def idctii(x, axes=None):
    if axes is None:
        axes = list(range(x.ndim))
    for ax in axes[::-1]:
        x = fftpack.idct(x, type=2, axis=ax, norm='ortho')
    return x