def load_balancers_list_all(**kwargs):
    result = {}
    netconn = __utils__['azurearm.get_client']('network', **kwargs)
    try:
        load_balancers = __utils__['azurearm.paged_object_to_list'](netconn
            .load_balancers.list_all())
        for load_balancer in load_balancers:
            result[load_balancer['name']] = load_balancer
    except CloudError as exc:
        __utils__['azurearm.log_cloud_error']('network', str(exc), **kwargs)
        result = {'error': str(exc)}
    return result