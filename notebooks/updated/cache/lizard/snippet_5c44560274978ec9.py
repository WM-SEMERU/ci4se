def destroy(zpool, force=False):
    res = __salt__['cmd.run_all'](__utils__['zfs.zpool_command'](command=
        'destroy', flags=['-f'] if force else None, target=zpool),
        python_shell=False)
    return __utils__['zfs.parse_command_result'](res, 'destroyed')