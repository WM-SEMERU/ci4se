def _fetch_option(cfg, ret_config, virtualname, attr_name):
    if isinstance(cfg, dict):
        c_cfg = cfg
    else:
        c_cfg = cfg('{0}'.format(virtualname), {})
    default_cfg_key = '{0}.{1}'.format(virtualname, attr_name)
    if not ret_config:
        if isinstance(cfg, dict):
            if default_cfg_key in cfg:
                return cfg[default_cfg_key]
            else:
                return c_cfg.get(attr_name)
        else:
            return c_cfg.get(attr_name, cfg(default_cfg_key))
    ret_cfg = cfg('{0}.{1}'.format(ret_config, virtualname), {})
    override_default_cfg_key = '{0}.{1}.{2}'.format(ret_config, virtualname,
        attr_name)
    override_cfg_default = cfg(override_default_cfg_key)
    ret_override_cfg = ret_cfg.get(attr_name, override_cfg_default)
    if ret_override_cfg:
        return ret_override_cfg
    return c_cfg.get(attr_name, cfg(default_cfg_key))