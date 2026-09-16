def read_band_blocks(self, blocksize=CHUNK_SIZE):
    band = self.filehandle
    shape = band.shape
    token = tokenize(blocksize, band)
    name = 'read_band-' + token
    dskx = dict()
    if len(band.block_shapes) != 1:
        raise NotImplementedError('Bands with multiple shapes not supported.')
    else:
        chunks = band.block_shapes[0]

    def do_read(the_band, the_window, the_lock):
        with the_lock:
            return the_band.read(1, None, window=the_window)
    for ji, window in band.block_windows(1):
        dskx[(name,) + ji] = do_read, band, window, self.read_lock
    res = da.Array(dskx, name, shape=list(shape), chunks=chunks, dtype=band
        .dtypes[0])
    return DataArray(res, dims=('y', 'x'))