def image_predict(self, X):
    self._check_image(X)
    new_shape = X.shape[0] * X.shape[1] * X.shape[2],
    if len(X.shape) == 4:
        new_shape += X.shape[3],
    pixels = X.reshape(new_shape)
    predictions = self.classifier.predict(self._transform_input(pixels))
    return predictions.reshape(X.shape[0], X.shape[1], X.shape[2])