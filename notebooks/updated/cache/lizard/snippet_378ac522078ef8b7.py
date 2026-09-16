def delete_lb(kwargs=None, call=None):
    if call != 'function':
        raise SaltCloudSystemExit(
            'The delete_hc function must be called with -f or --function.')
    if not kwargs or 'name' not in kwargs:
        log.error('A name must be specified when deleting a health check.')
        return False
    name = kwargs['name']
    lb_conn = get_lb_conn(get_conn())
    __utils__['cloud.fire_event']('event', 'delete load_balancer',
        'salt/cloud/loadbalancer/deleting', args={'name': name}, sock_dir=
        __opts__['sock_dir'], transport=__opts__['transport'])
    try:
        result = lb_conn.destroy_balancer(lb_conn.get_balancer(name))
    except ResourceNotFoundError as exc:
        log.error('Load balancer %s was not found. Exception was: %s', name,
            exc, exc_info_on_loglevel=logging.DEBUG)
        return False
    __utils__['cloud.fire_event']('event', 'deleted load_balancer',
        'salt/cloud/loadbalancer/deleted', args={'name': name}, sock_dir=
        __opts__['sock_dir'], transport=__opts__['transport'])
    return result