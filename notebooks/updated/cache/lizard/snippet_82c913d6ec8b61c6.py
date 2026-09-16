def split(zpool, newzpool, **kwargs):
    opts = {}
    pool_properties = kwargs.get('properties', {})
    if kwargs.get('altroot', False):
        opts['-R'] = kwargs.get('altroot')
    res = __salt__['cmd.run_all'](__utils__['zfs.zpool_command'](command=
        'split', opts=opts, pool_properties=pool_properties, target=[zpool,
        newzpool]), python_shell=False)
    return __utils__['zfs.parse_command_result'](res, 'split')