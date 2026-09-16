def subvolume_create(name, dest=None, qgroupids=None):
    if qgroupids and type(qgroupids) is not list:
        raise CommandExecutionError('Qgroupids parameter must be a list')
    if dest:
        name = os.path.join(dest, name)
    if subvolume_exists(name):
        return False
    cmd = ['btrfs', 'subvolume', 'create']
    if type(qgroupids) is list:
        cmd.append('-i')
        cmd.extend(qgroupids)
    cmd.append(name)
    res = __salt__['cmd.run_all'](cmd)
    salt.utils.fsutils._verify_run(res)
    return True