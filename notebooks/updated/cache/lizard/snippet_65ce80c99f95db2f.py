def _predict(self, features):
    from sklearn.exceptions import NotFittedError
    try:
        prediction = self.kernel.predict_classes(features)[:, (0)]
    except NotFittedError:
        raise NotFittedError(
            "{} is not fitted yet. Call 'fit' with appropriate arguments before using this method."
            .format(type(self).__name__))
    return prediction