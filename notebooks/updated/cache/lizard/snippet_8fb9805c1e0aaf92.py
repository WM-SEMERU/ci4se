def _get_default_parameter_values(sam_template):
    default_values = {}
    parameter_definition = sam_template.get('Parameters', None)
    if not parameter_definition or not isinstance(parameter_definition, dict):
        LOG.debug('No Parameters detected in the template')
        return default_values
    for param_name, value in parameter_definition.items():
        if isinstance(value, dict) and 'Default' in value:
            default_values[param_name] = value['Default']
    LOG.debug('Collected default values for parameters: %s', default_values)
    return default_values