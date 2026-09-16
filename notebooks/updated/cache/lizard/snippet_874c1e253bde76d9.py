def avail_projects(call=None):
    if call == 'action':
        raise SaltCloudException(
            'The avail_projects function must be called with -f or --function.'
            )
    vm_ = get_configured_provider()
    manager = packet.Manager(auth_token=vm_['token'])
    ret = {}
    for project in manager.list_projects():
        ret[project.name] = project.__dict__
    return ret