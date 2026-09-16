def build_config(config_file=get_system_config_directory()):
    config = Config(config_file, allow_no_value=True)
    application_versions = find_applications_on_system()
    for item in application_versions.iteritems():
        if not config.has_option(Config.EXECUTABLES, item[0]):
            config.set(Config.EXECUTABLES, item[0], item[1])
    return config