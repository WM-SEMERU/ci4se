def set_app_name_for_pool(client, pool, name):
    if cmp_pkgrevno('ceph-common', '12.0.0') >= 0:
        cmd = ['ceph', '--id', client, 'osd', 'pool', 'application',
            'enable', pool, name]
        check_call(cmd)