def predict_proba(self, p):
    if p.size != p.shape[0]:
        p = p[:, (1)]
    calibrated_proba = np.zeros(p.shape[0])
    for i in range(self.calibration_map.shape[0]):
        calibrated_proba[np.logical_and(self.calibration_map[i, 1] <= p, 
            self.calibration_map[i, 0] > p)] = self.calibration_map[i, 2]
    return calibrated_proba