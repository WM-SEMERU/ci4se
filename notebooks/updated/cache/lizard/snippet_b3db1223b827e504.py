def _get_top_features(feature_names, coef, top, x):
    if isinstance(top, (list, tuple)):
        num_pos, num_neg = list(top)
        pos = _get_top_positive_features(feature_names, coef, num_pos, x)
        neg = _get_top_negative_features(feature_names, coef, num_neg, x)
    else:
        pos, neg = _get_top_abs_features(feature_names, coef, top, x)
    return pos, neg