def ring2nest(nside, ipix):
    ipix = np.atleast_1d(ipix).astype(np.int64, copy=False)
    return ring_to_nested(ipix, nside)