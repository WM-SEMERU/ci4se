def convolve2d_disk(fn, r, sig, nstep=200):
    r = np.array(r, ndmin=1)
    sig = np.array(sig, ndmin=1)
    rmin = r - sig
    rmax = r + sig
    rmin[rmin < 0] = 0
    delta = (rmax - rmin) / nstep
    redge = rmin[..., np.newaxis] + delta[..., np.newaxis] * np.linspace(0,
        nstep, nstep + 1)
    rp = 0.5 * (redge[(...), 1:] + redge[(...), :-1])
    dr = redge[(...), 1:] - redge[(...), :-1]
    fnv = fn(rp)
    r = r.reshape(r.shape + (1,))
    cphi = -np.ones(dr.shape)
    m = ((rp + r) / sig < 1) | (r == 0)
    rrp = r * rp
    sx = r ** 2 + rp ** 2 - sig ** 2
    cphi[~m] = sx[~m] / (2 * rrp[~m])
    dphi = 2 * np.arccos(cphi)
    v = rp * fnv * dphi * dr / (np.pi * sig * sig)
    s = np.sum(v, axis=-1)
    return s