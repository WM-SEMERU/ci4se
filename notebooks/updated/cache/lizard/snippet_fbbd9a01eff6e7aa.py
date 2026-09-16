def igrf_value(lat, lon, alt=0.0, year=2005.0):
    X, Y, Z, F = calculate.igrf12syn(0, year, 1, alt, lat, lon)
    D = FACT * np.arctan2(Y, X)
    H = np.sqrt(X * X + Y * Y)
    I = FACT * np.arctan2(Z, H)
    return D, I, H, X, Y, Z, F