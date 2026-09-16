def route_create_or_update(name, address_prefix, next_hop_type, route_table,
    resource_group, next_hop_ip_address=None, **kwargs):
    netconn = __utils__['azurearm.get_client']('network', **kwargs)
    try:
        rt_model = __utils__['azurearm.create_object_model']('network',
            'Route', address_prefix=address_prefix, next_hop_type=
            next_hop_type, next_hop_ip_address=next_hop_ip_address, **kwargs)
    except TypeError as exc:
        result = {'error': 'The object model could not be built. ({0})'.
            format(str(exc))}
        return result
    try:
        route = netconn.routes.create_or_update(resource_group_name=
            resource_group, route_table_name=route_table, route_name=name,
            route_parameters=rt_model)
        route.wait()
        rt_result = route.result()
        result = rt_result.as_dict()
    except CloudError as exc:
        __utils__['azurearm.log_cloud_error']('network', str(exc), **kwargs)
        result = {'error': str(exc)}
    except SerializationError as exc:
        result = {'error': 'The object model could not be parsed. ({0})'.
            format(str(exc))}
    return result