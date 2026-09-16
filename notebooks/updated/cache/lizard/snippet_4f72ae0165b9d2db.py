def remove_nan_observations(x, y, z):
    r
    x_ = x[~np.isnan(z)]
    y_ = y[~np.isnan(z)]
    z_ = z[~np.isnan(z)]
    return x_, y_, z_