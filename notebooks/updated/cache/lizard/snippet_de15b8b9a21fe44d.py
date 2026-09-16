def boundaries_lonlat(healpix_index, step, nside, order='ring'):
    healpix_index = np.asarray(healpix_index, dtype=np.int64)
    step = int(step)
    if step < 1:
        raise ValueError('step must be at least 1')
    frac = np.linspace(0.0, 1.0, step + 1)[:-1]
    dx = np.hstack([1 - frac, np.repeat(0, step), frac, np.repeat(1, step)])
    dy = np.hstack([np.repeat(1, step), 1 - frac, np.repeat(0, step), frac])
    healpix_index, dx, dy = np.broadcast_arrays(healpix_index.reshape(-1, 1
        ), dx, dy)
    lon, lat = healpix_to_lonlat(healpix_index.ravel(), nside, dx.ravel(),
        dy.ravel(), order=order)
    lon = lon.reshape(-1, 4 * step)
    lat = lat.reshape(-1, 4 * step)
    return lon, lat