def prepare_gag_lsm(self, lsm_precip_data_var, lsm_precip_type,
    interpolation_type=None):
    if self.l2g is None:
        raise ValueError('LSM converter not loaded ...')
    for unif_precip_card in self.UNIFORM_PRECIP_CARDS:
        self.project_manager.deleteCard(unif_precip_card, self.db_session)
    with tmp_chdir(self.project_manager.project_directory):
        out_gage_file = '{0}.gag'.format(self.project_manager.name)
        self.l2g.lsm_precip_to_gssha_precip_gage(out_gage_file,
            lsm_data_var=lsm_precip_data_var, precip_type=lsm_precip_type)
        self._update_simulation_end_from_lsm()
        self.set_simulation_duration(self.simulation_end - self.
            simulation_start)
        self.add_precip_file(out_gage_file, interpolation_type)
        self.l2g.xd.close()