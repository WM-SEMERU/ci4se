def com(points, masses=None):
    if masses is None:
        return np.average(points, axis=0)
    else:
        return np.average(points, axis=0, weights=masses)