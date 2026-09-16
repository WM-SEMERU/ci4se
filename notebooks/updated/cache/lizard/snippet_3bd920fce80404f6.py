def get_coef(clf, label_id, scale=None):
    if len(clf.coef_.shape) == 2:
        coef = _dense_1d(clf.coef_[label_id])
    elif len(clf.coef_.shape) == 1:
        if label_id != 0:
            raise ValueError('Unexpected label_id %s for 1D coefficient' %
                label_id)
        coef = _dense_1d(clf.coef_)
    elif len(clf.coef_.shape) == 0:
        coef = np.array([clf.coef_])
    else:
        raise ValueError('Unexpected clf.coef_ shape: %s' % clf.coef_.shape)
    if scale is not None:
        if coef.shape != scale.shape:
            raise ValueError(
                'scale shape is incorrect: expected %s, got %s' % (coef.
                shape, scale.shape))
        not_nan = ~np.isnan(scale)
        coef = coef.copy()
        coef[not_nan] *= scale[not_nan]
    if not has_intercept(clf):
        return coef
    if label_id == 0 and not isinstance(clf.intercept_, np.ndarray):
        bias = clf.intercept_
    else:
        bias = clf.intercept_[label_id]
    return np.hstack([coef, bias])