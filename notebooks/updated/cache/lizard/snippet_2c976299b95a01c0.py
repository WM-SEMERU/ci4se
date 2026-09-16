def _get_tdm(self, m):
    m = np.atleast_2d(m)
    assert len(m.shape) == 2
    tdm = crtomo.tdMan(grid=self.grid, tempdir=self.tempdir)
    tdm.configs.add_to_configs(self.configs)
    pid_mag = tdm.parman.add_data(m[(0), :])
    tdm.register_magnitude_model(pid_mag)
    if m.shape[0] == 2:
        pid_pha = tdm.parman.add_data(m[(1), :])
    else:
        pid_pha = tdm.parman.add_data(np.zeros(m.shape[1]))
    tdm.register_phase_model(pid_pha)
    return tdm