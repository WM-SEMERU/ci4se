def fit_proba(clf, X, y_proba, expand_factor=10, sample_weight=None,
    shuffle=True, random_state=None, **fit_params):
    X, y, sample_weight = expanded_X_y_sample_weights(X, y_proba,
        expand_factor=expand_factor, sample_weight=sample_weight, shuffle=
        shuffle, random_state=random_state)
    fit_params = with_sample_weight(clf, sample_weight, fit_params)
    clf.fit(X, y, **fit_params)
    return clf