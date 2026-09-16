def _root_mean_square_error(y, y_pred, w):
    return np.sqrt(np.average((y_pred - y) ** 2, weights=w))