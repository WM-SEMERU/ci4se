def list_variables(self):
    station_codes = self._get_station_codes()
    station_codes = self._apply_features_filter(station_codes)
    variables = self._list_variables(station_codes)
    if hasattr(self, '_variables') and self.variables is not None:
        variables.intersection_update(set(self.variables))
    return list(variables)