def _build_vertex_data(self):
    grid = self._grid
    w = 1.0 / grid[1]
    h = 1.0 / grid[0]
    quad = np.array([[0, 0, 0], [w, 0, 0], [w, h, 0], [0, 0, 0], [w, h, 0],
        [0, h, 0]], dtype=np.float32)
    quads = np.empty((grid[1], grid[0], 6, 3), dtype=np.float32)
    quads[:] = quad
    mgrid = np.mgrid[0.0:grid[1], 0.0:grid[0]].transpose(1, 2, 0)
    mgrid = mgrid[:, :, (np.newaxis), :]
    mgrid[..., 0] *= w
    mgrid[..., 1] *= h
    quads[(...), :2] += mgrid
    tex_coords = quads.reshape(grid[1] * grid[0] * 6, 3)
    tex_coords = np.ascontiguousarray(tex_coords[:, :2])
    vertices = tex_coords * self.size
    self._subdiv_position.set_data(vertices.astype('float32'))
    self._subdiv_texcoord.set_data(tex_coords.astype('float32'))