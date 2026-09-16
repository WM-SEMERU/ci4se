def monthly_cooling_design_days_020(self):
    if self.monthly_found is False or self._monthly_db_20 == [
        ] or self._monthly_wb_20 == []:
        return []
    else:
        db_conds = [DryBulbCondition(x, y) for x, y in zip(self.
            _monthly_db_20, self._monthly_db_range_50)]
        hu_conds = [HumidityCondition('Wetbulb', x, self.
            _stand_press_at_elev) for x in self._monthly_wb_20]
        ws_conds = self.monthly_wind_conditions
        sky_conds = self.monthly_clear_sky_conditions
        return [DesignDay('2% Cooling Design Day for {}'.format(self.
            _months[i]), 'SummerDesignDay', self._location, db_conds[i],
            hu_conds[i], ws_conds[i], sky_conds[i]) for i in xrange(12)]