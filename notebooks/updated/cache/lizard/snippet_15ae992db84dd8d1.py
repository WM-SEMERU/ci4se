def set_vertex_colors(self, colors, indexed=None):
    colors = _fix_colors(np.asarray(colors))
    if indexed is None:
        if colors.ndim != 2:
            raise ValueError('colors must be 2D if indexed is None')
        if colors.shape[0] != self.n_vertices:
            raise ValueError('incorrect number of colors %s, expected %s' %
                (colors.shape[0], self.n_vertices))
        self._vertex_colors = colors
        self._vertex_colors_indexed_by_faces = None
    elif indexed == 'faces':
        if colors.ndim != 3:
            raise ValueError('colors must be 3D if indexed is "faces"')
        if colors.shape[0] != self.n_faces:
            raise ValueError('incorrect number of faces')
        self._vertex_colors = None
        self._vertex_colors_indexed_by_faces = colors
    else:
        raise ValueError('indexed must be None or "faces"')