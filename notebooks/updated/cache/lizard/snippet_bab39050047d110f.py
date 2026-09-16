def read_exodus(filename, animate_mode_shapes=True, apply_displacements=
    True, displacement_magnitude=1.0, enabled_sidesets=None):
    reader = vtk.vtkExodusIIReader()
    reader.SetFileName(filename)
    reader.UpdateInformation()
    reader.SetAnimateModeShapes(animate_mode_shapes)
    reader.SetApplyDisplacements(apply_displacements)
    reader.SetDisplacementMagnitude(displacement_magnitude)
    if enabled_sidesets is None:
        enabled_sidesets = list(range(reader.GetNumberOfSideSetArrays()))
    for sideset in enabled_sidesets:
        if isinstance(sideset, int):
            name = reader.GetSideSetArrayName(sideset)
        elif isinstance(sideset, str):
            name = sideset
        else:
            raise ValueError('Could not parse sideset ID/name: {}'.format(
                sideset))
        reader.SetSideSetArrayStatus(name, 1)
    reader.Update()
    return vtki.wrap(reader.GetOutput())