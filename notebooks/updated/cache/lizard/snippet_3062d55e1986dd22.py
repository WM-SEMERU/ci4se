def _read_ascii(self):
    header_str = ''
    with open(self.path) as f:
        for line in f:
            if line.startswith('#'):
                header_str += line
    self._read_header(header_str)
    data = np.loadtxt(self.path, delimiter=',', unpack=True, ndmin=1)
    n_dim = len(self.dimensions)
    data = {stat: data[n_dim + i] for i, stat in enumerate(self.statistics)}
    data_shape = [dim.n_bins for dim in self.dimensions]
    data = {k: v.reshape(data_shape) for k, v in data.items()}
    self.data = data