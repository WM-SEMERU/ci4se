def check_variable_attributes(self, ds):
    return [self._has_var_attr(ds, 'platform', 'long_name',
        'Station Long Name'), self._has_var_attr(ds, 'platform',
        'short_name', 'Station Short Name'), self._has_var_attr(ds,
        'platform', 'source', 'Platform Type'), self._has_var_attr(ds,
        'platform', 'ioos_name', 'Station ID'), self._has_var_attr(ds,
        'platform', 'wmo_id', 'Station WMO ID'), self._has_var_attr(ds,
        'platform', 'comment', 'Station Description')]