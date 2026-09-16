def _compute_distance(self, rup, dists, C):
    rval = np.sqrt(dists.repi ** 2 + C['h'] ** 2)
    return C['c1'] * np.log10(rval)