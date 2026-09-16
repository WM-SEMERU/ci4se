def _replace_constant_methods(self):
    self.cumulative_distribution = self._constant_cumulative_distribution
    self.percent_point = self._constant_percent_point
    self.probability_density = self._constant_probability_density
    self.sample = self._constant_sample