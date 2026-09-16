def closestDirectDistance(arr, ksize=30, dtype=np.uint16):
    out = np.zeros_like(arr, dtype=dtype)
    _calc(out, arr, ksize)
    return out