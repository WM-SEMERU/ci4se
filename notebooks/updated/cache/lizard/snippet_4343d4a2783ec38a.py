def route_filter_delete(name, resource_group, **kwargs):
    result = False
    netconn = __utils__['azurearm.get_client']('network', **kwargs)
    try:
        route_filter = netconn.route_filters.delete(route_filter_name=name,
            resource_group_name=resource_group)
        route_filter.wait()
        result = True
    except CloudError as exc:
        __utils__['azurearm.log_cloud_error']('network', str(exc), **kwargs)
    return result