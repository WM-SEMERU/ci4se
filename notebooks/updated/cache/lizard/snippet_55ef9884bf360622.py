def optimal_slope(cn, n, dt, z, i):
    dh = np.nansum(-cn / (n * dt)) * z[i] + np.nansum(cn / (n * dt) * z[i + n])
    return dh