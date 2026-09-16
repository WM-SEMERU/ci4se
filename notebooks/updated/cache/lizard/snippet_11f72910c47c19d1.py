def explain_permutation_importance(estimator, vec=None, top=_TOP,
    target_names=None, targets=None, feature_names=None, feature_re=None,
    feature_filter=None):
    coef = estimator.feature_importances_
    coef_std = estimator.feature_importances_std_
    return get_feature_importance_explanation(estimator, vec, coef,
        coef_std=coef_std, feature_names=feature_names, feature_filter=
        feature_filter, feature_re=feature_re, top=top, description=
        DESCRIPTION_SCORE_DECREASE + estimator.caveats_, is_regression=
        isinstance(estimator.wrapped_estimator_, RegressorMixin))