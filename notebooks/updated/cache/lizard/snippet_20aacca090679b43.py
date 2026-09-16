def get_gruneisen_parameter(self, temperature=None, structure=None, quad=None):
    return np.trace(self.get_tgt(temperature, structure, quad)) / 3.0