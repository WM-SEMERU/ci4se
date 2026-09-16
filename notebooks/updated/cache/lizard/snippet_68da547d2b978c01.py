def _worst_case_generation(self, worst_case_scale_factors, modes):
    self.timeseries.generation_fluctuating = pd.DataFrame({'solar': [
        worst_case_scale_factors['{}_feedin_pv'.format(mode)] for mode in
        modes], 'wind': [worst_case_scale_factors['{}_feedin_other'.format(
        mode)] for mode in modes]}, index=self.timeseries.timeindex)
    self.timeseries.generation_dispatchable = pd.DataFrame({'other': [
        worst_case_scale_factors['{}_feedin_other'.format(mode)] for mode in
        modes]}, index=self.timeseries.timeindex)