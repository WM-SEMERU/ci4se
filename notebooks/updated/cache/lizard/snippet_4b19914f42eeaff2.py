def rm_(name, force=False, volumes=False, **kwargs):
    kwargs = __utils__['args.clean_kwargs'](**kwargs)
    stop_ = kwargs.pop('stop', False)
    timeout = kwargs.pop('timeout', None)
    auto_remove = False
    if kwargs:
        __utils__['args.invalid_kwargs'](kwargs)
    if state(name) == 'running' and not (force or stop_):
        raise CommandExecutionError(
            "Container '{0}' is running, use force=True to forcibly remove this container"
            .format(name))
    if stop_ and not force:
        inspect_results = inspect_container(name)
        try:
            auto_remove = inspect_results['HostConfig']['AutoRemove']
        except KeyError:
            log.error(
                'Failed to find AutoRemove in inspect results, Docker API may have changed. Full results: %s'
                , inspect_results)
        stop(name, timeout=timeout)
    pre = ps_(all=True)
    if not auto_remove:
        _client_wrapper('remove_container', name, v=volumes, force=force)
    _clear_context()
    return [x for x in pre if x not in ps_(all=True)]