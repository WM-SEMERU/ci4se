def logs(name, **kwargs):
    kwargs = __utils__['args.clean_kwargs'](**kwargs)
    if 'stream' in kwargs:
        raise SaltInvocationError("The 'stream' argument is not supported")
    try:
        kwargs['since'] = int(kwargs['since'])
    except KeyError:
        pass
    except (ValueError, TypeError):
        if HAS_TIMELIB:
            try:
                kwargs['since'] = timelib.strtodatetime(kwargs['since'])
            except Exception as exc:
                log.warning(
                    "docker.logs: Failed to parse '%s' using timelib: %s",
                    kwargs['since'], exc)
    return salt.utils.stringutils.to_unicode(_client_wrapper('logs', name,
        **kwargs))