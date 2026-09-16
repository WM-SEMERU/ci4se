def ashraeiam(aoi, b=0.05):
    iam = 1 - b * (1 / np.cos(np.radians(aoi)) - 1)
    aoi_gte_90 = np.full_like(aoi, False, dtype='bool')
    np.greater_equal(np.abs(aoi), 90, where=~np.isnan(aoi), out=aoi_gte_90)
    iam = np.where(aoi_gte_90, 0, iam)
    iam = np.maximum(0, iam)
    if isinstance(iam, pd.Series):
        iam = pd.Series(iam, index=aoi.index)
    return iam