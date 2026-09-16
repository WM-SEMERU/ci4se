def H_iso(x, params):
    r = np.sum(x[:3] ** 2)
    return 0.5 * np.sum(x[3:] ** 2) - Grav * params[0] / (params[1] + np.
        sqrt(params[1] ** 2 + r))