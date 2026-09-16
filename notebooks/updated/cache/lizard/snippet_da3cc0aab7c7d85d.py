def _compute_magnitude_term(self, C, mag):
    fmag = C['c0'] + C['c1'] * mag
    if mag <= 5.5:
        return fmag
    elif mag > 6.5:
        return fmag + C['c2'] * (mag - 5.5) + C['c3'] * (mag - 6.5)
    else:
        return fmag + C['c2'] * (mag - 5.5)