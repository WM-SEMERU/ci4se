def update_vertices(self, mask, inverse=None):
    if self.is_empty:
        return
    mask = np.asanyarray(mask)
    if mask.dtype.name == 'bool' and mask.all() or len(mask
        ) == 0 or self.is_empty:
        return
    if inverse is None:
        inverse = np.zeros(len(self.vertices), dtype=np.int64)
        if mask.dtype.kind == 'b':
            inverse[mask] = np.arange(mask.sum())
        elif mask.dtype.kind == 'i':
            inverse[mask] = np.arange(len(mask))
        else:
            inverse = None
    if inverse is not None and util.is_shape(self.faces, (-1, 3)):
        self.faces = inverse[self.faces.reshape(-1)].reshape((-1, 3))
    self.visual.update_vertices(mask)
    cached_normals = self._cache['vertex_normals']
    self.vertices = self.vertices[mask]
    if util.is_shape(cached_normals, (-1, 3)):
        try:
            self.vertex_normals = cached_normals[mask]
        except BaseException:
            pass