def calc_observable_fraction(self, distance_modulus):
    observable_fraction = self.isochrone.observableFraction(self.mask,
        distance_modulus)
    if not observable_fraction.sum() > 0:
        msg = 'No observable fraction'
        msg += '\n' + str(self.source.params)
        logger.error(msg)
        raise ValueError(msg)
    return observable_fraction