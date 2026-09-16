def compute_K_factors(self, spacing=None, configs=None, numerical=False,
    elem_file=None, elec_file=None):
    if configs is None:
        use_configs = self.configs
    else:
        use_configs = configs
    if numerical:
        settings = {'elem': elem_file, 'elec': elec_file, 'rho': 100}
        K = edfK.compute_K_numerical(use_configs, settings)
    else:
        K = edfK.compute_K_analytical(use_configs, spacing=spacing)
    return K