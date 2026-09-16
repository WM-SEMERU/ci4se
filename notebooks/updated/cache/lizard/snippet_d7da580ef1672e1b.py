def view(self, single_components=False):
    if self.is_rgb:
        img = self.rgb_to_vector()
    else:
        img = self
    dtype = img.dtype
    shape = img.shape[::-1]
    if img.has_components or single_components == True:
        shape = list(shape) + [img.components]
    libfn = utils.get_lib_fn('toNumpy%s' % img._libsuffix)
    memview = libfn(img.pointer)
    return np.asarray(memview).view(dtype=dtype).reshape(shape).view(np.ndarray
        ).T