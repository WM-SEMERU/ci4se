def get_dataset(self, key, info):
    if self._channel != key.name:
        return
    logger.debug('Reading %s.', key.name)
    quantification_value = 10000.0
    jp2 = glymur.Jp2k(self.filename)
    bitdepth = 0
    for seg in jp2.codestream.segment:
        try:
            bitdepth = max(bitdepth, seg.bitdepth[0])
        except AttributeError:
            pass
    jp2.dtype = np.uint8 if bitdepth <= 8 else np.uint16
    data = da.from_delayed(delayed(jp2.read)(), jp2.shape, jp2.dtype)
    data = data.rechunk(CHUNK_SIZE) / quantification_value * 100
    proj = DataArray(data, dims=['y', 'x'])
    proj.attrs = info.copy()
    proj.attrs['units'] = '%'
    proj.attrs['platform_name'] = self.platform_name
    return proj