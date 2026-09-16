def spline_factors(u):
    X = np.array([(1.0 - u) ** 3, 4 - 6.0 * u ** 2 + 3.0 * u ** 3, 1.0 + 
        3.0 * u + 3.0 * u ** 2 - 3.0 * u ** 3, u ** 3]) * (1.0 / 6)
    return X