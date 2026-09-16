def _compute_magnitude_scaling(self, mag, C):
    dmag = mag - 6.0
    return C['B2'] * dmag + C['B3'] * dmag ** 2.0