def exists(zpool):
    res = __salt__['cmd.run_all'](__utils__['zfs.zpool_command'](command=
        'list', target=zpool), python_shell=False, ignore_retcode=True)
    return res['retcode'] == 0