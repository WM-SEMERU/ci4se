def load_configs(envvar_prefix, path=None):
    conf = {}
    if path:
        conf.update(from_file(path))
    else:
        conf.update(from_envvar_file(envvar_prefix + 'SETTINGS'))
    conf.update(from_envvars(prefix=envvar_prefix))
    return conf