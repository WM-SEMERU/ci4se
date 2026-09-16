def napoleon_to_sphinx(docstring, **config_params):
    if 'napoleon_use_param' not in config_params:
        config_params['napoleon_use_param'] = False
    if 'napoleon_use_rtype' not in config_params:
        config_params['napoleon_use_rtype'] = False
    config = Config(**config_params)
    return str(GoogleDocstring(docstring, config))