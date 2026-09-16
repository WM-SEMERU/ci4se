def minmax(arrays, masks=None, dtype=None, out=None, zeros=None, scales=
    None, weights=None, nmin=1, nmax=1):
    return generic_combine(intl_combine.minmax_method(nmin, nmax), arrays,
        masks=masks, dtype=dtype, out=out, zeros=zeros, scales=scales,
        weights=weights)