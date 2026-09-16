def iterate(config_file_path=None, config=None, variables=None, tags=None,
    validate=True, validate_only=False, with_diff=False):
    if not isinstance(variables or {}, dict):
        raise TypeError(ERRORS['variables_not_dict'])
    if not isinstance(tags or [], list):
        raise TypeError(ERRORS['tags_not_list'])
    config = _get_config(config_file_path, config)
    if validate or validate_only:
        _validate_config_schema(config)
    if validate_only:
        logger.info('Config file validation completed successfully!')
        sys.exit(0)
    repex_vars = _merge_variables(config['variables'], variables or {})
    repex_tags = tags or []
    logger.debug('Chosen tags: %s', repex_tags)
    for path in config['paths']:
        _process_path(path, repex_tags, repex_vars, with_diff)