def routes_list(route_table, resource_group, **kwargs):
    result = {}
    netconn = __utils__['azurearm.get_client']('network', **kwargs)
    try:
        routes = __utils__['azurearm.paged_object_to_list'](netconn.routes.
            list(resource_group_name=resource_group, route_table_name=
            route_table))
        for route in routes:
            result[route['name']] = route
    except CloudError as exc:
        __utils__['azurearm.log_cloud_error']('network', str(exc), **kwargs)
        result = {'error': str(exc)}
    return result