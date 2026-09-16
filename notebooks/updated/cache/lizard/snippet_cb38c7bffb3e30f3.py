def spline_functions(lower_points, upper_points, degree=3):
    lower_xx = np.array([pp[0] for pp in lower_points])
    lower_yy = np.array([pp[1] for pp in lower_points])
    upper_xx = np.array([pp[0] for pp in upper_points])
    upper_yy = np.array([pp[1] for pp in upper_points])
    lower_spline = UnivariateSpline(lower_xx, lower_yy, k=degree, s=0)
    upper_spline = UnivariateSpline(upper_xx, upper_yy, k=degree, s=0)

    def lower(x):
        return lower_spline(x)

    def upper(x):
        return upper_spline(x)
    return {'lower': lower, 'upper': upper}