def filename(self, fname, timestep=None, suffix='', force_legacy=False):
    if timestep is not None:
        fname += '{:05d}'.format(timestep)
    fname += suffix
    if not force_legacy and self.hdf5:
        fpath = self.hdf5 / fname
    else:
        fpath = self.par['ioin']['output_file_stem'] + '_' + fname
        fpath = self.path / fpath
    return fpath