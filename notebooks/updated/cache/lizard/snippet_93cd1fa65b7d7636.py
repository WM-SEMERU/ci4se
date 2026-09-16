def fit(self, X, y):
    X, event, time = check_arrays_survival(X, y)
    weights = ipc_weights(event, time)
    super().fit(X, numpy.log(time), sample_weight=weights)
    return self