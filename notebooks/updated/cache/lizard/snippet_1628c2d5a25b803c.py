def cylinders_from_ellipses(ellipses):
    ellipses = np.asarray(ellipses)
    ellipsoids = np.zeros((ellipses.shape[0], 10))
    ellipsoids[:, ([0, 1, 2, 4, 5, 7])] = ellipses
    ellipsoids[:, (3)] = 100000.0
    return ellipsoids