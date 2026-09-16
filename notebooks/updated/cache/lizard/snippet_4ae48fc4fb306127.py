def _tukey(self, x, threshold):
    vals = x.values[~np.isnan(x.values)]
    try:
        q1, q3 = np.percentile(vals, [25, 75])
        iqr = q3 - q1
        low_bound = q1 - iqr * threshold
        high_bound = q3 + iqr * threshold
        outliers = np.where((vals > high_bound) | (vals < low_bound))
    except:
        outliers = []
    return outliers