def mesh(self, vertices=None, faces=None, vertex_colors=None, face_colors=
    None, color=(0.5, 0.5, 1.0), fname=None, meshdata=None):
    self._configure_3d()
    if fname is not None:
        if not all(x is None for x in (vertices, faces, meshdata)):
            raise ValueError(
                'vertices, faces, and meshdata must be None if fname is not None'
                )
        vertices, faces = read_mesh(fname)[:2]
    if meshdata is not None:
        if not all(x is None for x in (vertices, faces, fname)):
            raise ValueError(
                'vertices, faces, and fname must be None if fname is not None')
    else:
        meshdata = MeshData(vertices, faces)
    mesh = scene.Mesh(meshdata=meshdata, vertex_colors=vertex_colors,
        face_colors=face_colors, color=color, shading='smooth')
    self.view.add(mesh)
    self.view.camera.set_range()
    return mesh