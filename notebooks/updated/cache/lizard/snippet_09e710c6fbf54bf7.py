def parameter_vector(self):
    return np.array([getattr(self, k) for k in self.parameter_names])