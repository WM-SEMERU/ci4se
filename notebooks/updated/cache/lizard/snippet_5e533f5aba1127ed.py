def _get_project_conf():
    config_settings = {}
    project_root = find_vcs_root('.')
    if project_root is None:
        return config_settings
    for conf_dir in PROJECT_CONF_DIRS:
        conf_dir = conf_dir.lstrip('./')
        joined_dir = os.path.join(project_root, conf_dir
            ) if conf_dir else project_root
        joined_glob = os.path.join(joined_dir, PROJECT_CONF)
        conf_files = glob.glob(joined_glob)
        if conf_files:
            break
    else:
        conf_files = []
    for conf_file in conf_files:
        try:
            with io.open(conf_file, encoding='utf-8') as input_file:
                loaded_settings = yaml.safe_load(input_file)
        except EnvironmentError:
            logger.warning('Failed to load config from %s', conf_file)
        else:
            logger.info('Config loaded from %s', conf_file)
            config_settings.update(loaded_settings)
    return config_settings