def detach_disk(name=None, kwargs=None, call=None):
    if call != 'action':
        raise SaltCloudSystemExit(
            'The detach_Disk action must be called with -a or --action.')
    if not name:
        log.error('Must specify an instance name.')
        return False
    if not kwargs or 'disk_name' not in kwargs:
        log.error('Must specify a disk_name to detach.')
        return False
    node_name = name
    disk_name = kwargs['disk_name']
    conn = get_conn()
    node = conn.ex_get_node(node_name)
    disk = conn.ex_get_volume(disk_name)
    __utils__['cloud.fire_event']('event', 'detach disk',
        'salt/cloud/disk/detaching', args={'name': node_name, 'disk_name':
        disk_name}, sock_dir=__opts__['sock_dir'], transport=__opts__[
        'transport'])
    result = conn.detach_volume(disk, node)
    __utils__['cloud.fire_event']('event', 'detached disk',
        'salt/cloud/disk/detached', args={'name': node_name, 'disk_name':
        disk_name}, sock_dir=__opts__['sock_dir'], transport=__opts__[
        'transport'])
    return result