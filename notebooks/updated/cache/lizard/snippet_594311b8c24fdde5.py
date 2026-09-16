def _find_metadata_vars(self, ds, refresh=False):
    if self._metadata_vars.get(ds, None) and refresh is False:
        return self._metadata_vars[ds]
    self._metadata_vars[ds] = []
    for name, var in ds.variables.items():
        if name in self._find_ancillary_vars(ds
            ) or name in self._find_coord_vars(ds):
            continue
        if name in ('platform_name', 'station_name', 'instrument_name',
            'station_id', 'platform_id', 'surface_altitude'):
            self._metadata_vars[ds].append(name)
        elif getattr(var, 'cf_role', '') != '':
            self._metadata_vars[ds].append(name)
        elif getattr(var, 'standard_name', None) is None and len(var.dimensions
            ) == 0:
            self._metadata_vars[ds].append(name)
    return self._metadata_vars[ds]