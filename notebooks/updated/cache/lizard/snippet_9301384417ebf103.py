def bear_rhumb(ra1, dec1, ra2, dec2):
    phi1 = np.radians(dec1)
    phi2 = np.radians(dec2)
    lambda1 = np.radians(ra1)
    lambda2 = np.radians(ra2)
    dlambda = lambda2 - lambda1
    dpsi = np.log(np.tan(np.pi / 4 + phi2 / 2) / np.tan(np.pi / 4 + phi1 / 2))
    theta = np.arctan2(dlambda, dpsi)
    return np.degrees(theta)