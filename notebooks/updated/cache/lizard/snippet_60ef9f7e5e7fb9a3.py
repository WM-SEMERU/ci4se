def _downscaling(self, hr_array, meta_info, interp='linear', smooth=True):
    if self.cm_size_y is None and self.cm_size_x is None:
        return hr_array, None
    rescale = self._get_rescale_factors(hr_array.shape[1:3], meta_info)
    if smooth:
        sigma = (0,) + tuple(int(1 / x) for x in rescale) + (0,)
        hr_array = scipy.ndimage.gaussian_filter(hr_array, sigma)
    lr_array = scipy.ndimage.interpolation.zoom(hr_array, (1.0,) + rescale +
        (1.0,), order=INTERP_METHODS.index(interp), mode='nearest')
    return lr_array, rescale