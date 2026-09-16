def _compute_term1(self, C, mag):
    mag_diff = mag - 6
    return C['c2'] * mag_diff + C['c3'] * mag_diff ** 2