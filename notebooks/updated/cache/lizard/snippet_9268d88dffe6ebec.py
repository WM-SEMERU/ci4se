def log_prior(self):
    for p, b in zip(self.parameter_vector, self.parameter_bounds):
        if b[0] is not None and p < b[0]:
            return -np.inf
        if b[1] is not None and p > b[1]:
            return -np.inf
    return 0.0