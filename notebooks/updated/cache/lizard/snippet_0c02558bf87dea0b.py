def _compute_f5(self, C, pga_rock):
    return C['a10'] + C['a11'] * np.log(pga_rock + C['c5'])