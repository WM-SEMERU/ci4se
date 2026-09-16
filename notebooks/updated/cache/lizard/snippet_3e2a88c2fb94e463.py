def noise_uniform(self, lower_bound, upper_bound):
    assert upper_bound > lower_bound
    nu = self.sym.sym('nu_{:d}'.format(len(self.scope['nu'])))
    self.scope['nu'].append(nu)
    return lower_bound + nu * (upper_bound - lower_bound)