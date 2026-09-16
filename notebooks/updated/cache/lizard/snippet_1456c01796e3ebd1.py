def pvsyst_celltemp(self, poa_global, temp_air, wind_speed=1.0):
    kwargs = _build_kwargs(['eta_m', 'alpha_absorption'], self.
        module_parameters)
    return pvsyst_celltemp(poa_global, temp_air, wind_speed, model_params=
        self.racking_model, **kwargs)