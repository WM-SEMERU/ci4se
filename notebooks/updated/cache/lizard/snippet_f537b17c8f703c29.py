def load_config(path, env_var, default_path=None, exit_on_config_errors=True):
    if path is None:
        return {}
    if default_path is None:
        import inspect
        previous_frame = inspect.getframeinfo(inspect.currentframe().f_back)
        log.warning(
            "The function '%s()' defined in '%s' is not yet using the new 'default_path' argument to `salt.config.load_config()`. As such, the '%s' environment variable will be ignored"
            , previous_frame.function, previous_frame.filename, env_var)
        default_path = DEFAULT_MASTER_OPTS['conf_file']
    env_path = os.environ.get(env_var, path)
    if not env_path or not os.path.isfile(env_path):
        env_path = path
    if path != default_path:
        env_path = path
    path = env_path
    if not os.path.isfile(path):
        template = '{0}.template'.format(path)
        if os.path.isfile(template):
            log.debug('Writing %s based on %s', path, template)
            with salt.utils.files.fopen(path, 'w') as out:
                with salt.utils.files.fopen(template, 'r') as ifile:
                    ifile.readline()
                    out.write(ifile.read())
    opts = {}
    if salt.utils.validate.path.is_readable(path):
        try:
            opts = _read_conf_file(path)
            opts['conf_file'] = path
        except salt.exceptions.SaltConfigurationError as error:
            log.error(error)
            if exit_on_config_errors:
                sys.exit(salt.defaults.exitcodes.EX_GENERIC)
    else:
        log.debug('Missing configuration file: %s', path)
    return opts