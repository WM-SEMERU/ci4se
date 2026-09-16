def _mprotate(ang, lny, pool, order):
    targ_args = list()
    slsize = np.int(np.floor(lny / ncores))
    for t in range(ncores):
        ymin = t * slsize
        ymax = (t + 1) * slsize
        if t == ncores - 1:
            ymax = lny
        targ_args.append((ymin, ymax, ang, order))
    pool.map(_rotate, targ_args)