def staged_predict(self, X):
    check_is_fitted(self, 'estimators_')
    if not hasattr(self, 'scale_'):
        for y in self._staged_decision_function(X):
            yield self._scale_prediction(y.ravel())
    else:
        for y in self._dropout_staged_decision_function(X):
            yield self._scale_prediction(y.ravel())