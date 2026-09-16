def start(vm_name, call=None):
    if call != 'action':
        raise SaltCloudSystemExit(
            'The start action must be called with -a or --action.')
    conn = get_conn()
    __utils__['cloud.fire_event']('event', 'start instance',
        'salt/cloud/{0}/starting'.format(vm_name), args={'name': vm_name},
        sock_dir=__opts__['sock_dir'], transport=__opts__['transport'])
    result = conn.ex_start_node(conn.ex_get_node(vm_name))
    __utils__['cloud.fire_event']('event', 'start instance',
        'salt/cloud/{0}/started'.format(vm_name), args={'name': vm_name},
        sock_dir=__opts__['sock_dir'], transport=__opts__['transport'])
    return result