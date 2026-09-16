def add(zpool, *vdevs, **kwargs):
    flags = []
    target = []
    if kwargs.get('force', False):
        flags.append('-f')
    target.append(zpool)
    target.extend(vdevs)
    res = __salt__['cmd.run_all'](__utils__['zfs.zpool_command'](command=
        'add', flags=flags, target=target), python_shell=False)
    ret = __utils__['zfs.parse_command_result'](res, 'added')
    if ret['added']:
        ret['vdevs'] = _clean_vdev_config(__salt__['zpool.status'](zpool=
            zpool)[zpool]['config'][zpool])
    return ret