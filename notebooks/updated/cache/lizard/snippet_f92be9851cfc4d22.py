def _diff_bounds(bounds, coord):
    try:
        return bounds[:, (1)] - bounds[:, (0)]
    except IndexError:
        diff = np.diff(bounds, axis=0)
        return xr.DataArray(diff, dims=coord.dims, coords=coord.coords)