def _get_colors(self, name):
    try:
        counts = {'face': len(self.mesh.faces), 'vertex': len(self.mesh.
            vertices)}
        count = counts[name]
    except AttributeError:
        count = None
    key_colors = str(name) + '_colors'
    key_crc = key_colors + '_crc'
    if key_colors in self._data:
        return self._data[key_colors]
    elif key_colors in self._cache:
        colors = self._cache[key_colors]
        if colors.crc() != self._cache[key_crc]:
            if name == 'face':
                self.face_colors = colors
            elif name == 'vertex':
                self.vertex_colors = colors
            else:
                raise ValueError('unsupported name!!!')
            self._cache.verify()
    elif self.kind is None:
        colors = np.tile(self.defaults['material_diffuse'], (count, 1))
    elif self.kind == 'vertex' and name == 'face':
        colors = vertex_to_face_color(vertex_colors=self.vertex_colors,
            faces=self.mesh.faces)
    elif self.kind == 'face' and name == 'vertex':
        colors = face_to_vertex_color(mesh=self.mesh, face_colors=self.
            face_colors)
    else:
        raise ValueError('self.kind not accepted values!!')
    if count is not None and colors.shape != (count, 4):
        raise ValueError('face colors incorrect shape!')
    colors = caching.tracked_array(colors)
    self._cache[key_colors] = colors
    self._cache[key_crc] = colors.crc()
    return colors