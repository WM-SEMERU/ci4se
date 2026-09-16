def get_configs(config_filepath, local_filepath_override=''):
    global_config = read_config(config_filepath)
    local_filepath = get_local_config_filepath(config_filepath, True)
    if local_filepath_override:
        local_filepath = local_filepath_override
    local_config = read_config(local_filepath)
    return global_config, local_config