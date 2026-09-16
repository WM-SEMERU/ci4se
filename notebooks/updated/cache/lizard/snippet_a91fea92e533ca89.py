def get_data(self, datakind, integnum):
    if integnum < 0 or integnum >= self.n_integrations:
        raise ValueError('illegal integration number %d' % integnum)
    size = self.sizeinfo.get(datakind)
    if size is None:
        raise ValueError('unrecognized data kind "%s"' % datakind)
    dtype = _datatypes[datakind]
    offset = self.headsize + integnum * self.intsize
    dslice = self.mmdata[offset:offset + size]
    data = np.fromstring(dslice, dtype=dtype)
    if datakind == 'crossData.bin':
        data = data.reshape((self.n_baselines, self.n_channels, len(self.
            crosspols)))
    elif datakind == 'autoData.bin':
        data = data.reshape((self.n_antennas, self.n_channels, 2))
    elif datakind == 'flags.bin':
        data = data.reshape((self.n_baselines + self.n_antennas, self.
            n_channels, len(self.crosspols)))
    return data