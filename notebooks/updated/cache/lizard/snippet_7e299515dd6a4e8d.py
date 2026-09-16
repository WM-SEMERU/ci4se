def route_filter_rule_delete(name, route_filter, resource_group, **kwargs):
    result = False
    netconn = __utils__['azurearm.get_client']('network', **kwargs)
    try:
        rule = netconn.route_filter_rules.delete(resource_group_name=
            resource_group, route_filter_name=route_filter, rule_name=name)
        rule.wait()
        result = True
    except CloudError as exc:
        __utils__['azurearm.log_cloud_error']('network', str(exc), **kwargs)
    return result