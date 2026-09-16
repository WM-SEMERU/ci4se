def _get_distance_scaling_term(self, C, mag, rrup):
    return (C['r1'] + C['r2'] * mag) * np.log10(rrup + C['r3'])