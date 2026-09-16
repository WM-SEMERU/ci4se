def _check_scalar_vertical_extents(self, ds, z_variable):
    vert_min = ds.geospatial_vertical_min
    vert_max = ds.geospatial_vertical_max
    msgs = []
    total = 2
    zvalue = ds.variables[z_variable][:].item()
    if not np.isclose(vert_min, vert_max):
        msgs.append(
            'geospatial_vertical_min != geospatial_vertical_max for scalar depth values, %s != %s'
             % (vert_min, vert_max))
    if not np.isclose(vert_max, zvalue):
        msgs.append('geospatial_vertical_max != %s values, %s != %s' % (
            z_variable, vert_max, zvalue))
    return Result(BaseCheck.MEDIUM, (total - len(msgs), total),
        'geospatial_vertical_extents_match', msgs)