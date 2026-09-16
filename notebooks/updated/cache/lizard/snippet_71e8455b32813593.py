def get_val(self, x):
    interval, mean, std = self.probability_map[x]
    new_val = norm.rvs(mean, std)
    return new_val