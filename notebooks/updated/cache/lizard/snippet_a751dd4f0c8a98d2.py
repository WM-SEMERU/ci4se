def rfftn(a, s=None, axes=None, norm=None):
    unitary = _unitary(norm)
    if unitary:
        a = asarray(a)
        s, axes = _cook_nd_args(a, s, axes)
    output = mkl_fft.rfftn_numpy(a, s, axes)
    if unitary:
        n_tot = prod(asarray(s, dtype=output.dtype))
        output *= 1 / sqrt(n_tot)
    return output