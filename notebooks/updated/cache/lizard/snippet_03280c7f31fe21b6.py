def authenticate(realm, authid, details):
    global _start
    global _waiting
    import json
    ticket = json.loads(details['ticket'])
    if 'application_name' not in ticket and 'version' not in ticket:
        raise ApplicationError(
            'could not start the authentication of an app,             field application_name or version is missing'
            )
    application_name = ticket['application_name']
    version = ticket['version']
    required_components = ticket['required_components'
        ] if 'required_components' in ticket else {}
    if not _try_to_start_app(application_name, version, required_components):
        ready_defered = defer.Deferred()
        ready_defered.addCallback(defer_try_start_app, application_name=
            application_name, version=version, required_components=
            required_components)
        _waiting[application_name]['defer'] = ready_defered
        yield ready_defered
    print('[MESTR] start app: ', _start)
    print('[MESTR] waiting app: ', _waiting)
    for k in _start:
        if k in _waiting:
            _waiting = remove_element(_waiting, k)
    returnValue('backend')