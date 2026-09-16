def run_dynamic_structure_factor(self, Qpoints, T, atomic_form_factor_func=
    None, scattering_lengths=None, freq_min=None, freq_max=None):
    self.init_dynamic_structure_factor(Qpoints, T, atomic_form_factor_func=
        atomic_form_factor_func, scattering_lengths=scattering_lengths,
        freq_min=freq_min, freq_max=freq_max)
    self._dynamic_structure_factor.run()