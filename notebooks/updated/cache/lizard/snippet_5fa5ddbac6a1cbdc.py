def _score(estimator, X_test, y_test, scorer):
    if y_test is None:
        score = scorer(estimator, X_test)
    else:
        score = scorer(estimator, X_test, y_test)
    if not isinstance(score, numbers.Number):
        raise ValueError(
            'scoring must return a number, got %s (%s) instead.' % (str(
            score), type(score)))
    return score