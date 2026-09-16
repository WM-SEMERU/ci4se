def _select_basin_model(self, vs30):
    if self.CONSTS['SJ']:
        return np.exp(5.359 - 1.102 * np.log(vs30))
    else:
        return np.exp(7.089 - 1.144 * np.log(vs30))