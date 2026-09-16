def get_auxiliary_coordinate_variables(ds):
    aux_vars = []
    for ncvar in ds.get_variables_by_attributes(coordinates=lambda x:
        isinstance(x, basestring)):
        referenced_variables = ncvar.coordinates.split(' ')
        for referenced_variable in referenced_variables:
            if (referenced_variable in ds.variables and referenced_variable
                 not in aux_vars):
                aux_vars.append(referenced_variable)
    for variable in get_axis_variables(ds):
        if variable not in aux_vars:
            aux_vars.append(variable)
    coordinate_standard_names = ['time', 'longitude', 'latitude', 'height',
        'depth', 'altitude']
    coordinate_standard_names += DIMENSIONLESS_VERTICAL_COORDINATES
    for ncvar in ds.get_variables_by_attributes(standard_name=lambda x: x in
        coordinate_standard_names):
        if ncvar.name not in aux_vars:
            aux_vars.append(ncvar.name)
    ret_val = []
    for aux_var in aux_vars:
        if ds.variables[aux_var].dimensions == (aux_var,):
            continue
        ret_val.append(aux_var)
    return ret_val