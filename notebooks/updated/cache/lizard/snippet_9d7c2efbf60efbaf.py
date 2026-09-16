def get_mapping_variable(variable_name, variables_mapping):
    try:
        return variables_mapping[variable_name]
    except KeyError:
        raise exceptions.VariableNotFound('{} is not found.'.format(
            variable_name))