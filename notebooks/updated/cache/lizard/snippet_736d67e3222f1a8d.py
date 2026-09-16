def get_exclude_paths(registry):
    regexes = registry.settings.get('pyramid_swagger.skip_validation',
        registry.settings.get('pyramid_swagger.exclude_paths',
        DEFAULT_EXCLUDED_PATHS))
    if not isinstance(regexes, list) and not isinstance(regexes, tuple):
        regexes = [regexes]
    return [re.compile(r) for r in regexes]