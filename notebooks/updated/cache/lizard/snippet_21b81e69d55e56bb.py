def bounding_ellipsoids(points, pointvol=0.0, vol_dec=0.5, vol_check=2.0):
    if not HAVE_KMEANS:
        raise ValueError(
            'scipy.cluster.vq.kmeans2 is required to compute ellipsoid decompositions.'
            )
    ell = bounding_ellipsoid(points, pointvol=pointvol)
    ells = _bounding_ellipsoids(points, ell, pointvol=pointvol, vol_dec=
        vol_dec, vol_check=vol_check)
    return MultiEllipsoid(ells=ells)