def predict(self, X_feat, X_seq):
    X_seq = np.expand_dims(X_seq, axis=1)
    return self._get_other_var(X_feat, X_seq, variable='y_pred')