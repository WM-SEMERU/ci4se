def normalized_energy_at_conditions(self, pH, V):
    return self.energy_at_conditions(pH, V) * self.normalization_factor