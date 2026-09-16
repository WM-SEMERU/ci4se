def format_var_name(variable, var_list):
    z_index = None
    if variable in var_list:
        var_name = variable
    elif variable.ljust(6, '_') in var_list:
        var_name = variable.ljust(6, '_')
    elif any([(variable in v_sub.split('_')) for v_sub in var_list]):
        var_name = var_list[[(variable in v_sub.split('_')) for v_sub in
            var_list].index(True)]
        z_index = var_name.split('_').index(variable)
    else:
        raise KeyError('{0} not found in {1}'.format(variable, var_list))
    return var_name, z_index