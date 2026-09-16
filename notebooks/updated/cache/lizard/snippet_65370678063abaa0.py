def cartesian(points):
    points = np.asanyarray(points)
    ndim = points.ndim
    if ndim == 1:
        points = points.reshape((1, points.size))
    d = points.sum(axis=1)
    x = 0.5 * (2 * points[:, (1)] + points[:, (2)]) / d
    y = np.sqrt(3.0) / 2 * points[:, (2)] / d
    out = np.vstack([x, y]).T
    if ndim == 1:
        return out.reshape((2,))
    return out