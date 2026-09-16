def with_fallback(self, config, resolve=True):
    if isinstance(config, ConfigTree):
        result = ConfigTree.merge_configs(copy.deepcopy(config), copy.
            deepcopy(self))
    else:
        from . import ConfigFactory
        result = ConfigTree.merge_configs(ConfigFactory.parse_file(config,
            resolve=False), copy.deepcopy(self))
    if resolve:
        from . import ConfigParser
        ConfigParser.resolve_substitutions(result)
    return result