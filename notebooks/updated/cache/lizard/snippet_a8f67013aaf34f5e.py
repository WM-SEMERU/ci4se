def fit(self, y_true_cal=None, y_prob_cal=None):
    if self.calibration:
        self.cal = ROCConvexHull()
        self.cal.fit(y_true_cal, y_prob_cal[:, (1)])