def get_capacity_vol(self, min_voltage=None, max_voltage=None,
    use_overall_normalization=True):
    pairs_in_range = self._select_in_voltage_range(min_voltage, max_voltage)
    normalization_vol = (self.normalization_volume if 
        use_overall_normalization or len(pairs_in_range) == 0 else
        pairs_in_range[-1].vol_discharge)
    return sum([pair.mAh for pair in pairs_in_range]
        ) / normalization_vol * 1e+24 / N_A