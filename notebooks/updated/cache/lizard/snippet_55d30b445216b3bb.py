def covariance_matrix(self):
    a = N.dot(self.U, self.sigma)
    cv = N.dot(a, a.T)
    return cv