def get_environment():
    section = _ENVIRONMENT_SECTION_NAME
    sys_cfg = _read_config(_SYSTEM_CONFIG_FILE)
    sys_env = dict(sys_cfg.items(section)) if sys_cfg.has_section(section
        ) else {}
    usr_cfg = _read_config(_USER_CONFIG_FILE)
    usr_env = dict(usr_cfg.items(section)) if usr_cfg.has_section(section
        ) else {}
    for k in usr_env.keys():
        sys_env[k] = usr_env[k]
    return sys_env