def nphase_border(im, include_diagonals=False):
    r
    if im.ndim != im.squeeze().ndim:
        warnings.warn('Input image conains a singleton axis:' + str(im.
            shape) + ' Reduce dimensionality with np.squeeze(im) to avoid' +
            ' unexpected behavior.')
    ndim = len(np.shape(im))
    if ndim not in [2, 3]:
        raise NotImplementedError('Function only works for 2d and 3d images')
    im = np.pad(im, pad_width=1, mode='edge')
    stack = _make_stack(im, include_diagonals)
    stack.sort()
    out = np.ones_like(im)
    for k in range(np.shape(stack)[ndim])[1:]:
        if ndim == 2:
            mask = stack[:, :, (k)] != stack[:, :, (k - 1)]
        elif ndim == 3:
            mask = stack[:, :, :, (k)] != stack[:, :, :, (k - 1)]
        out += mask
    if ndim == 2:
        return out[1:-1, 1:-1].copy()
    else:
        return out[1:-1, 1:-1, 1:-1].copy()