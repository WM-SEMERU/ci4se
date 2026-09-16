def overlapping_spheres(shape: List[int], radius: int, porosity: float,
    iter_max: int=10, tol: float=0.01):
    r
    shape = sp.array(shape)
    if sp.size(shape) == 1:
        shape = sp.full((3,), int(shape))
    ndim = (shape != 1).sum()
    s_vol = ps_disk(radius).sum() if ndim == 2 else ps_ball(radius).sum()
    bulk_vol = sp.prod(shape)
    N = int(sp.ceil((1 - porosity) * bulk_vol / s_vol))
    im = sp.random.random(size=shape)
    f = lambda N: spim.distance_transform_edt(im > N / bulk_vol) < radius
    g = lambda im: 1 - im.sum() / sp.prod(shape)
    N_low, N_high = N, 4 * N
    for i in range(iter_max):
        N = sp.mean([N_high, N_low], dtype=int)
        err = g(f(N)) - porosity
        if err > 0:
            N_low = N
        else:
            N_high = N
        if abs(err) <= tol:
            break
    return ~f(N)