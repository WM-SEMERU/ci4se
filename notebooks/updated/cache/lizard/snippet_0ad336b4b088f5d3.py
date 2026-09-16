def convert(model, feature_names, target):
    if not _HAS_SKLEARN:
        raise RuntimeError(
            'scikit-learn not found. scikit-learn conversion API is disabled.')
    _sklearn_util.check_expected_type(model, LogisticRegression)
    _sklearn_util.check_fitted(model, lambda m: hasattr(m, 'coef_'))
    return _MLModel(_convert(model, feature_names, target))