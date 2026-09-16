def get_instance(in_memory=False, config_path=None, config_name=None):
    global __conf
    if __conf is None:
        __conf = Configuration(in_memory=in_memory, custom_cfg_path=
            config_path, config_name=config_name)
    return __conf