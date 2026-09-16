def energy(self):
    return self.uncorrected_energy + np.sum(list(self.corrections.values()))