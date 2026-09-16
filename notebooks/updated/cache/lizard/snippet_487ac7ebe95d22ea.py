def round(self, value_array):
    value = value_array[0]
    rounded_value = self.domain[0]
    for domain_value in self.domain:
        if np.abs(domain_value - value) < np.abs(rounded_value - value):
            rounded_value = domain_value
    return [rounded_value]