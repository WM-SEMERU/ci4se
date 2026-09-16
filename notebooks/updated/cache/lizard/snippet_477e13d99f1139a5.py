def render_secrets(config_path, secret_path):
    with open(secret_path, 'r') as s_fh:
        secret_ini = anyconfig.load(s_fh, ac_parser='ini')
    with open(config_path, 'r') as c_fh:
        raw_cfg = c_fh.read()
    rendered_cfg = anytemplate.renders(raw_cfg, secret_ini, at_engine='jinja2')
    p_config = ProsperConfig(config_path)
    local_config = configparser.ConfigParser()
    local_config.optionxform = str
    local_config.read_string(rendered_cfg)
    p_config.local_config = local_config
    return p_config