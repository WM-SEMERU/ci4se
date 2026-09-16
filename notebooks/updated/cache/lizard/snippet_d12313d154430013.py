def _interpolate_cube(self, lon, lat, egy=None, interp_log=True):
    shape = np.broadcast(lon, lat, egy).shape
    lon = lon * np.ones(shape)
    lat = lat * np.ones(shape)
    theta = np.pi / 2.0 - np.radians(lat)
    phi = np.radians(lon)
    vals = []
    for i, _ in enumerate(self.hpx.evals):
        v = hp.pixelfunc.get_interp_val(self.counts[i], theta, phi, nest=
            self.hpx.nest)
        vals += [np.expand_dims(np.array(v, ndmin=1), -1)]
    vals = np.concatenate(vals, axis=-1)
    if egy is None:
        return vals.T
    egy = egy * np.ones(shape)
    if interp_log:
        xvals = utils.val_to_pix(np.log(self.hpx.evals), np.log(egy))
    else:
        xvals = utils.val_to_pix(self.hpx.evals, egy)
    vals = vals.reshape((-1, vals.shape[-1]))
    xvals = np.ravel(xvals)
    v = map_coordinates(vals, [np.arange(vals.shape[0]), xvals], order=1)
    return v.reshape(shape)