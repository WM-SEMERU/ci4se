def create_config(allow_insecure_config_file=False):
    config = Config()
    config.add_properties(GLOBAL_CONFIG_FILENAME)
    user_config_filename = get_user_config_filename()
    if (user_config_filename == LOCAL_CONFIG_FILENAME and not
        allow_insecure_config_file):
        verify_file_private(user_config_filename)
    config.add_properties(user_config_filename)
    return config