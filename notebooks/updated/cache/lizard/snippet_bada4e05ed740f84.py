def minion_config(path, env_var='SALT_MINION_CONFIG', defaults=None,
    cache_minion_id=False, ignore_config_errors=True, minion_id=None, role=
    'minion'):
    if defaults is None:
        defaults = DEFAULT_MINION_OPTS.copy()
    if not os.environ.get(env_var, None):
        salt_config_dir = os.environ.get('SALT_CONFIG_DIR', None)
        if salt_config_dir:
            env_config_file_path = os.path.join(salt_config_dir, 'minion')
            if salt_config_dir and os.path.isfile(env_config_file_path):
                os.environ[env_var] = env_config_file_path
    overrides = load_config(path, env_var, DEFAULT_MINION_OPTS['conf_file'])
    default_include = overrides.get('default_include', defaults[
        'default_include'])
    include = overrides.get('include', [])
    overrides.update(include_config(default_include, path, verbose=False,
        exit_on_config_errors=not ignore_config_errors))
    overrides.update(include_config(include, path, verbose=True,
        exit_on_config_errors=not ignore_config_errors))
    opts = apply_minion_config(overrides, defaults, cache_minion_id=
        cache_minion_id, minion_id=minion_id)
    opts['__role'] = role
    apply_sdb(opts)
    _validate_opts(opts)
    return opts