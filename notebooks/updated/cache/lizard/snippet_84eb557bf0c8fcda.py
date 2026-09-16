def set_vertices(self, verts=None, indexed=None, reset_normals=True):
    if indexed is None:
        if verts is not None:
            self._vertices = verts
        self._vertices_indexed_by_faces = None
    elif indexed == 'faces':
        self._vertices = None
        if verts is not None:
            self._vertices_indexed_by_faces = verts
    else:
        raise Exception("Invalid indexing mode. Accepts: None, 'faces'")
    if reset_normals:
        self.reset_normals()