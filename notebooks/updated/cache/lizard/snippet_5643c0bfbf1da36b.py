def sigmaclip(arrays, masks=None, dtype=None, out=None, zeros=None, scales=
    None, weights=None, low=3.0, high=3.0):
    return generic_combine(intl_combine.sigmaclip_method(low, high), arrays,
        masks=masks, dtype=dtype, out=out, zeros=zeros, scales=scales,
        weights=weights)