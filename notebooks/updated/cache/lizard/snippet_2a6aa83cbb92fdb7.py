def cumany(series):
    anys = series.expanding().apply(np.any).astype(bool)
    return anys