def fnc(ra, *args):
    repi = args[0]
    theta = args[1]
    mag = args[2]
    coeff = args[3]
    rb = rbf(ra, coeff, mag)
    t1 = ra ** 2 * np.sin(np.radians(theta)) ** 2
    t2 = rb ** 2 * np.cos(np.radians(theta)) ** 2
    xx = ra * rb / (t1 + t2) ** 0.5
    return xx - repi