def rollback(name, **kwargs):
    flags = []
    if kwargs.get('recursive_all', False):
        flags.append('-R')
    if kwargs.get('recursive', False):
        flags.append('-r')
    if kwargs.get('force', False):
        if kwargs.get('recursive_all', False) or kwargs.get('recursive', False
            ):
            flags.append('-f')
        else:
            log.warning(
                'zfs.rollback - force=True can only be used with recursive_all=True or recursive=True'
                )
    res = __salt__['cmd.run_all'](__utils__['zfs.zfs_command'](command=
        'rollback', flags=flags, target=name), python_shell=False)
    return __utils__['zfs.parse_command_result'](res, 'rolledback')