def tube(self, radius=None, scalars=None, capping=True, n_sides=20,
    radius_factor=10, preference='point', inplace=False):
    if n_sides < 3:
        n_sides = 3
    tube = vtk.vtkTubeFilter()
    tube.SetInputDataObject(self)
    tube.SetCapping(capping)
    if radius is not None:
        tube.SetRadius(radius)
    tube.SetNumberOfSides(n_sides)
    tube.SetRadiusFactor(radius_factor)
    if scalars is not None:
        if not isinstance(scalars, str):
            raise TypeError('Scalar array must be given as a string name')
        _, field = self.get_scalar(scalars, preference=preference, info=True)
        tube.SetInputArrayToProcess(0, 0, 0, field, scalars)
        tube.SetVaryRadiusToVaryRadiusByScalar()
    tube.Update()
    mesh = _get_output(tube)
    if inplace:
        self.overwrite(mesh)
    else:
        return mesh