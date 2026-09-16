def intersect(ray1, ray2, **kwargs):
    if not isinstance(ray1, Ray) or not isinstance(ray2, Ray):
        raise TypeError(
            'The input arguments must be instances of the Ray object')
    if ray1.dimension != ray2.dimension:
        raise ValueError('Dimensions of the input rays must be the same')
    tol = kwargs.get('tol', 1e-16)
    if ray1.dimension == 2:
        return _intersect2d(ray1, ray2, tol)
    elif ray1.dimension == 3:
        return _intersect3d(ray1, ray2, tol)
    else:
        raise NotImplementedError(
            'Intersection operation for the current type of rays has not been implemented yet'
            )