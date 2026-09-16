def _dense_fit(self, X, strategy, missing_values, fill_value):
    mask = _get_mask(X, missing_values)
    masked_X = ma.masked_array(X, mask=mask)
    if strategy == 'mean':
        mean_masked = np.ma.mean(masked_X, axis=0)
        mean = np.ma.getdata(mean_masked)
        mean[np.ma.getmask(mean_masked)] = np.nan
        return mean
    elif strategy == 'median':
        median_masked = np.ma.median(masked_X, axis=0)
        median = np.ma.getdata(median_masked)
        median[np.ma.getmaskarray(median_masked)] = np.nan
        return median
    elif strategy == 'most_frequent':
        X = X.transpose()
        mask = mask.transpose()
        if X.dtype.kind == 'O':
            most_frequent = np.empty(X.shape[0], dtype=object)
        else:
            most_frequent = np.empty(X.shape[0])
        for i, (row, row_mask) in enumerate(zip(X[:], mask[:])):
            row_mask = np.logical_not(row_mask).astype(np.bool)
            row = row[row_mask]
            most_frequent[i] = _most_frequent(row, np.nan, 0)
        return most_frequent
    elif strategy == 'constant':
        return np.full(X.shape[1], fill_value, dtype=X.dtype)