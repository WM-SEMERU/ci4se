def round(self, x):
    fraction, scaled_x, scale = self._get_fraction(x)
    if (fraction < self.minimum_stochastic_distance or 1 - fraction < self.
        minimum_stochastic_distance):
        result = round(x, self.precision)
    else:
        rounddown = fraction < self.random_generator.random()
        if rounddown:
            result = math.floor(scaled_x) / scale
        else:
            result = math.ceil(scaled_x) / scale
    self._record_roundoff_error(x, result)
    return result