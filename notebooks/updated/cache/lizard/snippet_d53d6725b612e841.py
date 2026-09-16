def resample_spline(points, smooth=0.001, count=None, degree=3):
    from scipy.interpolate import splprep, splev
    if count is None:
        count = len(points)
    points = np.asanyarray(points)
    closed = np.linalg.norm(points[0] - points[-1]) < tol.merge
    tpl = splprep(points.T, s=smooth, k=degree)[0]
    i = np.linspace(0.0, 1.0, count)
    resampled = np.column_stack(splev(i, tpl))
    if closed:
        shared = resampled[[0, -1]].mean(axis=0)
        resampled[0] = shared
        resampled[-1] = shared
    return resampled