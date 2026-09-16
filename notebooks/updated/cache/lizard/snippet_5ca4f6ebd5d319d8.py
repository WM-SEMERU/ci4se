def _get_deltas(self, sites):
    vs30 = sites.vs30
    delta_C = np.zeros(len(vs30))
    delta_C[(vs30 >= 360) & (vs30 < 760)] = 1
    delta_D = np.zeros(len(vs30))
    delta_D[vs30 < 360] = 1
    return delta_C, delta_D