def predict(self, y_prob):
    y_pred = np.floor(y_prob[:, (1)] + (1 - self.threshold_))
    return y_pred