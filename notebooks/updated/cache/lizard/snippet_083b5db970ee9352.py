def _distance(self):
    return np.average(self.min_kl, weights=self.f.weights)