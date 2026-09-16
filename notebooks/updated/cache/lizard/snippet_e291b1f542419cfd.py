def _mean_absolute_error(y, y_pred, w):
    return np.average(np.abs(y_pred - y), weights=w)