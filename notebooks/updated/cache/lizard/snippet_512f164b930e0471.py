def replace(self, **kwargs):
    new_kwargs = {}
    strict = kwargs.pop('strict', True)
    try:
        localpart = kwargs.pop('localpart')
    except KeyError:
        pass
    else:
        if localpart:
            localpart = nodeprep(localpart, allow_unassigned=not strict)
        new_kwargs['localpart'] = localpart
    try:
        domain = kwargs.pop('domain')
    except KeyError:
        pass
    else:
        if not domain:
            raise ValueError('domain must not be empty or None')
        new_kwargs['domain'] = nameprep(domain, allow_unassigned=not strict)
    try:
        resource = kwargs.pop('resource')
    except KeyError:
        pass
    else:
        if resource:
            resource = resourceprep(resource, allow_unassigned=not strict)
        new_kwargs['resource'] = resource
    if kwargs:
        raise TypeError('replace() got an unexpected keyword argument {!r}'
            .format(next(iter(kwargs))))
    return super()._replace(**new_kwargs)