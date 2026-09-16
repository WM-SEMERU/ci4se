def init(self, fle=None):
    if fle is None:
        fname = self.kwargs.get('gmpe_table', self.GMPE_TABLE)
        if fname is None:
            raise ValueError('You forgot to set GMPETable.GMPE_TABLE!')
        elif os.path.isabs(fname):
            self.GMPE_TABLE = fname
        else:
            self.GMPE_TABLE = os.path.abspath(os.path.join(self.GMPE_DIR,
                fname))
        fle = h5py.File(self.GMPE_TABLE, 'r')
    try:
        self.distance_type = fle['distance_type'].value
    except KeyError:
        self.distance_type = decode(fle['Distances'].attrs['metric'])
    self.REQUIRES_DISTANCES = set([self.distance_type])
    self.m_w = fle['Mw'][:]
    self.distances = fle['Distances'][:]
    self.imls = hdf_arrays_to_dict(fle['IMLs'])
    self.DEFINED_FOR_INTENSITY_MEASURE_TYPES = set(self._supported_imts())
    if 'SA' in self.imls and 'T' not in self.imls:
        raise ValueError('Spectral Acceleration must be accompanied by periods'
            )
    self._setup_standard_deviations(fle)
    if 'Amplification' in fle:
        self._setup_amplification(fle)