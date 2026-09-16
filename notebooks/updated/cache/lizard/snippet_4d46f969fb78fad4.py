def build_maya_environment(config, env=None, arg_paths=None):
    maya_env = MayaEnvironment()
    maya_env.exclude_pattern = config.get_list(Config.PATTERNS, 'exclude')
    maya_env.icon_extensions = config.get_list(Config.PATTERNS, 'icon_ext')
    env = get_environment_paths(config, env)
    if not env and arg_paths is None:
        return logger.info('Using maya factory environment setup.')
    logger.debug('Launching with addon paths: {}'.format(arg_paths))
    logger.debug('Launching with environment paths: {}'.format(env))
    if arg_paths:
        arg_paths = arg_paths.split(' ')
    for directory in flatten_combine_lists(env, arg_paths or ''):
        maya_env.traverse_path_for_valid_application_paths(directory)
    return maya_env