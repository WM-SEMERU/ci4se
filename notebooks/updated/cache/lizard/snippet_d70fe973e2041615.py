def find_configured_repository(name):
    parser = configparser.RawConfigParser()
    for config_file in [SYSTEM_CONFIG_FILE, USER_CONFIG_FILE]:
        config_file = parse_path(config_file)
        if os.path.isfile(config_file):
            logger.debug('Loading configuration file (%s) ..', format_path(
                config_file))
            parser.read(config_file)
    matching_repos = [r for r in parser.sections() if normalize_name(name) ==
        normalize_name(r)]
    if not matching_repos:
        msg = "No repositories found matching the name '%s'!"
        raise NoSuchRepositoryError(msg % name)
    elif len(matching_repos) != 1:
        msg = (
            "Multiple repositories found matching the name '%s'! (matches: %s)"
            )
        raise AmbiguousRepositoryNameError(msg % (name, concatenate(map(
            repr, matching_repos))))
    else:
        kw = {}
        options = dict(parser.items(matching_repos[0]))
        vcs_type = options.get('type', '').lower()
        local_path = options.get('local')
        if local_path:
            kw['local'] = parse_path(local_path)
        bare = options.get('bare', None)
        if bare is not None:
            kw['bare'] = coerce_boolean(bare)
        for name in ('remote', 'release-scheme', 'release-filter'):
            value = options.get(name)
            if value is not None:
                kw[name.replace('-', '_')] = value
        return repository_factory(vcs_type, **kw)