def configure_uwsgi(configurator_func):
    from .settings import ENV_CONF_READY, ENV_CONF_ALIAS, CONFIGS_MODULE_ATTR
    if os.environ.get(ENV_CONF_READY):
        del os.environ[ENV_CONF_READY]
        return None
    configurations = configurator_func()
    registry = OrderedDict()
    if not isinstance(configurations, (list, tuple)):
        configurations = [configurations]
    for conf_candidate in configurations:
        if not isinstance(conf_candidate, (Section, Configuration)):
            continue
        if isinstance(conf_candidate, Section):
            conf_candidate = conf_candidate.as_configuration()
        alias = conf_candidate.alias
        if alias in registry:
            raise ConfigurationError(
                "Configuration alias '%s' clashes with another configuration. Please change the alias."
                 % alias)
        registry[alias] = conf_candidate
    if not registry:
        raise ConfigurationError(
            "Callable passed into 'configure_uwsgi' must return 'Section' or 'Configuration' objects."
            )
    target_alias = os.environ.get(ENV_CONF_ALIAS)
    if not target_alias:
        last = sys.argv[-2:]
        if len(last) == 2 and last[0] == '--conf':
            target_alias = last[1]
    conf_list = list(registry.values())
    if target_alias:
        config = registry.get(target_alias)
        if config:
            section = config.sections[0]
            os.environ[ENV_CONF_READY] = '1'
            section.set_placeholder('config-alias', target_alias)
            config.print_ini()
    else:
        import inspect
        config_module = inspect.currentframe().f_back
        config_module.f_locals[CONFIGS_MODULE_ATTR] = conf_list
    return conf_list