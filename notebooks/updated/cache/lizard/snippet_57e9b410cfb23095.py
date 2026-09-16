def _get_base_rates(self, base_params):
    base_ipl_rate = base_params['CMT_EVENTS'] / (base_params['area'] *
        base_params['CMT_duration'])
    base_rate = np.zeros(self.number_magnitudes, dtype=float)
    for iloc in range(0, self.number_magnitudes):
        base_rate[iloc] = base_ipl_rate * calculate_taper_function(base_params
            ['CMT_moment'], self.threshold_moment[iloc], moment_function(
            base_params['corner_mag']), base_params['beta'])
    return base_rate