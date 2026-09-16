def predict(self, param_dict):
    encoder_dict = self._designmatrix_object.encoder
    X, col_names = self._designmatrix_object.run_encoder(param_dict,
        encoder_dict)
    Y_pred = self._compute_prediction(X)
    return Y_pred