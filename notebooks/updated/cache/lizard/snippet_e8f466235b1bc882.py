def __prepare_config(config, project_mapping, session_variables_set=None):
    raw_config_variables = config.pop('variables', {})
    raw_config_variables_mapping = utils.ensure_mapping_format(
        raw_config_variables)
    override_variables = utils.deepcopy_dict(project_mapping.get(
        'variables', {}))
    functions = project_mapping.get('functions', {})
    raw_config_variables_mapping.update(override_variables)
    if raw_config_variables_mapping:
        config['variables'] = raw_config_variables_mapping
    check_variables_set = set(raw_config_variables_mapping.keys())
    check_variables_set |= session_variables_set or set()
    prepared_config = prepare_lazy_data(config, functions,
        check_variables_set, cached=True)
    return prepared_config