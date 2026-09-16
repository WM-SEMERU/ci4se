def abs_energy(self, x):
    _energy = feature_calculators.abs_energy(x)
    logging.debug('abs energy by tsfresh calculated')
    return _energy