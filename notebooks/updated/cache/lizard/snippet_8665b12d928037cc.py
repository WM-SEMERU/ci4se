def list_subnets(call=None, kwargs=None):
    if kwargs is None:
        kwargs = {}
    if call == 'action':
        raise SaltCloudSystemExit(
            'The avail_sizes function must be called with -f or --function')
    netconn = get_conn(client_type='network')
    resource_group = kwargs.get('resource_group'
        ) or config.get_cloud_config_value('resource_group',
        get_configured_provider(), __opts__, search_global=False)
    if (not resource_group and 'group' in kwargs and 'resource_group' not in
        kwargs):
        resource_group = kwargs['group']
    if not resource_group:
        raise SaltCloudSystemExit('A resource group must be specified')
    if kwargs.get('network') is None:
        kwargs['network'] = config.get_cloud_config_value('network',
            get_configured_provider(), __opts__, search_global=False)
    if 'network' not in kwargs or kwargs['network'] is None:
        raise SaltCloudSystemExit('A "network" must be specified')
    ret = {}
    subnets = netconn.subnets.list(resource_group, kwargs['network'])
    for subnet in subnets:
        ret[subnet.name] = subnet.as_dict()
        ret[subnet.name]['ip_configurations'] = {}
        for ip_ in subnet.ip_configurations:
            comps = ip_.id.split('/')
            name = comps[-1]
            ret[subnet.name]['ip_configurations'][name] = ip_.as_dict()
            ret[subnet.name]['ip_configurations'][name]['subnet'] = subnet.name
        ret[subnet.name]['resource_group'] = resource_group
    return ret