def _populate_image_struct(self, image, imgdata):
    numrows, numcols, num_comps = imgdata.shape
    for k in range(num_comps):
        self._validate_nonzero_image_size(numrows, numcols, k)
    image.contents.x0 = self._cparams.image_offset_x0
    image.contents.y0 = self._cparams.image_offset_y0
    image.contents.x1 = image.contents.x0 + (numcols - 1
        ) * self._cparams.subsampling_dx + 1
    image.contents.y1 = image.contents.y0 + (numrows - 1
        ) * self._cparams.subsampling_dy + 1
    for k in range(0, num_comps):
        if self._cparams.rsiz in (core.OPJ_PROFILE_CINEMA_2K, core.
            OPJ_PROFILE_CINEMA_4K):
            image.contents.comps[k].prec = 12
            image.contents.comps[k].bpp = 12
        layer = np.ascontiguousarray(imgdata[:, :, (k)], dtype=np.int32)
        dest = image.contents.comps[k].data
        src = layer.ctypes.data
        ctypes.memmove(dest, src, layer.nbytes)
    return image