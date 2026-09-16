def resolve_capabilities(pkgs, refresh=False, root=None, **kwargs):
    if refresh:
        refresh_db(root)
    ret = list()
    for pkg in pkgs:
        if isinstance(pkg, dict):
            name = next(iter(pkg))
            version = pkg[name]
        else:
            name = pkg
            version = None
        if kwargs.get('resolve_capabilities', False):
            try:
                search(name, root=root, match='exact')
            except CommandExecutionError:
                try:
                    result = search(name, root=root, provides=True, match=
                        'exact')
                    if len(result) == 1:
                        name = next(iter(result.keys()))
                    elif len(result) > 1:
                        log.warning(
                            "Found ambiguous match for capability '%s'.", pkg)
                except CommandExecutionError as exc:
                    log.debug('Search failed with: %s', exc)
        if version:
            ret.append({name: version})
        else:
            ret.append(name)
    return ret