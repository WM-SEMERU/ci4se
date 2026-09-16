def predict_proba(self, X):
    X = self._check_array(X)
    self._check_method('predict_proba')
    if isinstance(X, da.Array):
        return X.map_blocks(_predict_proba, estimator=self.
            _postfit_estimator, dtype='float', chunks=(X.chunks[0], len(
            self._postfit_estimator.classes_)))
    elif isinstance(X, dd._Frame):
        return X.map_partitions(_predict_proba, estimator=self.
            _postfit_estimator)
    else:
        return _predict_proba(X, estimator=self._postfit_estimator)