def dtypes_out(ufunc, dtypes_in):
    sig = find_min_signature(ufunc, dtypes_in)
    tcs_out = sig.split('->')[1]
    return tuple(np.dtype(tc) for tc in tcs_out)