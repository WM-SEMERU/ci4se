def get_domain(self):
    if self.domain is None:
        return np.array([self.points.min(axis=0), self.points.max(axis=0)])
    return self.domain