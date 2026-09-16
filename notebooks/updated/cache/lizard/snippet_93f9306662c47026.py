def exists(name, **kwargs):
    opts = {}
    if kwargs.get('type', False):
        opts['-t'] = kwargs.get('type')
    res = __salt__['cmd.run_all'](__utils__['zfs.zfs_command'](command=
        'list', opts=opts, target=name), python_shell=False, ignore_retcode
        =True)
    return res['retcode'] == 0