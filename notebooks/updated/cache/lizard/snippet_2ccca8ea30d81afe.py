def write_image(self, img, extname=None, extver=None, compress=None,
    tile_dims=None, header=None):
    self.create_image_hdu(img, header=header, extname=extname, extver=
        extver, compress=compress, tile_dims=tile_dims)
    if header is not None:
        self[-1].write_keys(header)
        self[-1]._update_info()