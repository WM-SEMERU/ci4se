def Perc(poly, q, dist, sample=10000, **kws):
    shape = poly.shape
    poly = polynomials.flatten(poly)
    q = numpy.array(q) / 100.0
    dim = len(dist)
    Z = dist.sample(sample, **kws)
    if dim == 1:
        Z = Z,
        q = numpy.array([q])
    poly1 = poly(*Z)
    mi, ma = dist.range().reshape(2, dim)
    ext = numpy.mgrid[(slice(0, 2, 1),) * dim].reshape(dim, 2 ** dim).T
    ext = numpy.where(ext, mi, ma).T
    poly2 = poly(*ext)
    poly2 = numpy.array([_ for _ in poly2.T if not numpy.any(numpy.isnan(_))]
        ).T
    if poly2.shape:
        poly1 = numpy.concatenate([poly1, poly2], -1)
    samples = poly1.shape[-1]
    poly1.sort()
    out = poly1.T[numpy.asarray(q * (samples - 1), dtype=int)]
    out = out.reshape(q.shape + shape)
    return out