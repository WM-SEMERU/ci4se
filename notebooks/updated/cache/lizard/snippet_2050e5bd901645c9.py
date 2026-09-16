def save_to_tomodir(self, directory):
    self.create_tomodir(directory)
    self.grid.save_elem_file(directory + os.sep + 'grid/elem.dat')
    self.grid.save_elec_file(directory + os.sep + 'grid/elec.dat')
    if self.configs.configs is not None:
        self.configs.write_crmod_config(directory + os.sep +
            'config/config.dat')
    if self.assignments['forward_model'] is not None:
        self.parman.save_to_rho_file(directory + os.sep + 'rho/rho.dat',
            self.assignments['forward_model'][0], self.assignments[
            'forward_model'][1])
    self.crmod_cfg.write_to_file(directory + os.sep + 'exe/crmod.cfg')
    if self.assignments['measurements'] is not None:
        self.configs.write_crmod_volt(directory + os.sep + 'mod/volt.dat',
            self.assignments['measurements'])
    if self.assignments['sensitivities'] is not None:
        self._save_sensitivities(directory + os.sep + 'mod/sens')
    if self.assignments['potentials'] is not None:
        self._save_potentials(directory + os.sep + 'mod/pot')
    self.crtomo_cfg.write_to_file(directory + os.sep + 'exe/crtomo.cfg')
    if self.noise_model is not None:
        self.noise_model.write_crt_noisemod(directory + os.sep +
            'exe/crt.noisemod')
    if not os.path.isdir(directory + os.sep + 'inv'):
        os.makedirs(directory + os.sep + 'inv')