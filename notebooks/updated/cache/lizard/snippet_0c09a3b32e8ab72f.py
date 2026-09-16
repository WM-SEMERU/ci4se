def fit(self, y_prob, cost_mat, y_true):
    if self.calibration:
        cal = ROCConvexHull()
        cal.fit(y_true, y_prob[:, (1)])
        y_prob[:, (1)] = cal.predict_proba(y_prob[:, (1)])
        y_prob[:, (0)] = 1 - y_prob[:, (1)]
    thresholds = np.unique(y_prob)
    cost = np.zeros(thresholds.shape)
    for i in range(thresholds.shape[0]):
        pred = np.floor(y_prob[:, (1)] + (1 - thresholds[i]))
        cost[i] = cost_loss(y_true, pred, cost_mat)
    self.threshold_ = thresholds[np.argmin(cost)]
    return self