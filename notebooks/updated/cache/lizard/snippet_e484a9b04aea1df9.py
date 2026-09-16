def _compute_term2(self, C, mag, rjb):
    RM = np.sqrt(rjb ** 2 + C['c7'] ** 2 * np.exp(-1.25 + 0.227 * mag) ** 2)
    return -C['c4'] * np.log(RM) - (C['c5'] - C['c4']) * np.maximum(np.log(
        RM / 100), 0) - C['c6'] * RM