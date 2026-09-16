def create_loadbalancer(call=None, kwargs=None):
    if call != 'function':
        raise SaltCloudSystemExit(
            'The create_address function must be called with -f or --function.'
            )
    if kwargs is None:
        kwargs = {}
    conn = get_conn()
    datacenter_id = get_datacenter_id()
    loadbalancer = LoadBalancer(name=kwargs.get('name'), ip=kwargs.get('ip'
        ), dhcp=kwargs.get('dhcp'))
    response = conn.create_loadbalancer(datacenter_id, loadbalancer)
    _wait_for_completion(conn, response, 60, 'loadbalancer')
    return response