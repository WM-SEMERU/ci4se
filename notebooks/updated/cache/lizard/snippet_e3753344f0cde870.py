def calcparams_pvsyst(self, effective_irradiance, temp_cell):
    kwargs = _build_kwargs(['gamma_ref', 'mu_gamma', 'I_L_ref', 'I_o_ref',
        'R_sh_ref', 'R_sh_0', 'R_sh_exp', 'R_s', 'alpha_sc', 'EgRef',
        'irrad_ref', 'temp_ref', 'cells_in_series'], self.module_parameters)
    return calcparams_pvsyst(effective_irradiance, temp_cell, **kwargs)