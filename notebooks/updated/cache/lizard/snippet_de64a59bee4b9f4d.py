def h5features_convert(self, infile):
    with h5py.File(infile, 'r') as f:
        groups = list(f.keys())
    for group in groups:
        self._writer.write(Reader(infile, group).read(), self.groupname,
            append=True)