def _build_mesh(self, mesh_method, **kwargs):
    sma = kwargs.get('sma', self.sma)
    mesh_args = self.instantaneous_mesh_args
    if mesh_method == 'marching':
        ntriangles = kwargs.get('ntriangles', self.ntriangles)
        av = libphoebe.sphere_area_volume(*mesh_args, larea=True, lvolume=True)
        delta = _estimate_delta(ntriangles, av['larea'])
        new_mesh = libphoebe.sphere_marching_mesh(*mesh_args, delta=delta,
            full=True, max_triangles=ntriangles * 2, vertices=True,
            triangles=True, centers=True, vnormals=True, tnormals=True,
            cnormals=False, vnormgrads=True, cnormgrads=False, areas=True,
            volume=True, init_phi=self.mesh_init_phi)
        new_mesh['volume'] = av['lvolume']
        new_mesh['area'] = av['larea']
        scale = sma
    else:
        raise NotImplementedError("mesh_method '{}' is not supported".
            format(mesh_method))
    return new_mesh, scale