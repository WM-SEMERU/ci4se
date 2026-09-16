def solve_ng(self, structure, wavelength_step=0.01, filename='ng.dat'):
    r
    wl_nom = structure._wl
    self.solve(structure)
    n_ctrs = self.n_effs
    structure.change_wavelength(wl_nom - wavelength_step)
    self.solve(structure)
    n_bcks = self.n_effs
    structure.change_wavelength(wl_nom + wavelength_step)
    self.solve(structure)
    n_frws = self.n_effs
    n_gs = []
    for n_ctr, n_bck, n_frw in zip(n_ctrs, n_bcks, n_frws):
        n_gs.append(n_ctr - wl_nom * (n_frw - n_bck) / (2 * wavelength_step))
    if filename:
        with open(self._modes_directory + filename, 'w') as fs:
            fs.write('# Mode idx, Group index\n')
            for idx, n_g in enumerate(n_gs):
                fs.write('%i,%.3f\n' % (idx, np.round(n_g.real, 3)))
    return n_gs