def gradient(self, y_true, y_pred):
    return np.sign(np.subtract(y_pred, y_true))