def _accuracy_in_session(self, sess, other_var, X_feat, X_seq, y):
    y_pred = self._predict_in_session(sess, other_var, X_feat, X_seq)
    return ce.mse(y_pred, y)