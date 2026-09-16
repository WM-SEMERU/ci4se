def network_interfaces_list(resource_group, **kwargs):
    result = {}
    netconn = __utils__['azurearm.get_client']('network', **kwargs)
    try:
        nics = __utils__['azurearm.paged_object_to_list'](netconn.
            network_interfaces.list(resource_group_name=resource_group))
        for nic in nics:
            result[nic['name']] = nic
    except CloudError as exc:
        __utils__['azurearm.log_cloud_error']('network', str(exc), **kwargs)
        result = {'error': str(exc)}
    return result