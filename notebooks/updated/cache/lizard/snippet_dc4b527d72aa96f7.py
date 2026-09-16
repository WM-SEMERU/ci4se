def _worst_case_load(self, worst_case_scale_factors,
    peakload_consumption_ratio, modes):
    sectors = ['residential', 'retail', 'industrial', 'agricultural']
    lv_power_scaling = np.array([worst_case_scale_factors['lv_{}_load'.
        format(mode)] for mode in modes])
    mv_power_scaling = np.array([worst_case_scale_factors['mv_{}_load'.
        format(mode)] for mode in modes])
    lv = {(sector, 'lv'): (peakload_consumption_ratio[sector] *
        lv_power_scaling) for sector in sectors}
    mv = {(sector, 'mv'): (peakload_consumption_ratio[sector] *
        mv_power_scaling) for sector in sectors}
    self.timeseries.load = pd.DataFrame({**lv, **mv}, index=self.timeseries
        .timeindex)