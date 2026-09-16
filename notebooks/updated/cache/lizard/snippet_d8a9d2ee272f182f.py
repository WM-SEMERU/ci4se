def f1(y_true, y_pred, round=True):
    y_true, y_pred = _mask_value_nan(y_true, y_pred)
    if round:
        y_true = np.round(y_true)
        y_pred = np.round(y_pred)
    return skm.f1_score(y_true, y_pred)