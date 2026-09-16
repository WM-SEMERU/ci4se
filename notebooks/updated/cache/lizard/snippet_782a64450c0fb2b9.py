def update_settings(self, kwargs_model={}, kwargs_constraints={},
    kwargs_likelihood={}, lens_add_fixed=[], source_add_fixed=[],
    lens_light_add_fixed=[], ps_add_fixed=[], cosmo_add_fixed=[],
    lens_remove_fixed=[], source_remove_fixed=[], lens_light_remove_fixed=[
    ], ps_remove_fixed=[], cosmo_remove_fixed=[], change_source_lower_limit
    =None, change_source_upper_limit=None):
    self._updateManager.update_options(kwargs_model, kwargs_constraints,
        kwargs_likelihood)
    self._updateManager.update_fixed(self._lens_temp, self._source_temp,
        self._lens_light_temp, self._ps_temp, self._cosmo_temp,
        lens_add_fixed, source_add_fixed, lens_light_add_fixed,
        ps_add_fixed, cosmo_add_fixed, lens_remove_fixed,
        source_remove_fixed, lens_light_remove_fixed, ps_remove_fixed,
        cosmo_remove_fixed)
    self._updateManager.update_limits(change_source_lower_limit,
        change_source_upper_limit)
    return 0