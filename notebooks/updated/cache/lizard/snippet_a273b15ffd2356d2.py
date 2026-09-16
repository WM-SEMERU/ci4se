def gen_trace_planes(self, ridx):
    with h5py.File(self.source_file, 'r') as hdf5:
        for idx in ridx:
            trace = '{:s}/{:s}'.format(self.idx_set['sec'], str(idx))
            plane = hdf5[trace + '/RupturePlanes'][:].astype('float64')
            yield trace, plane