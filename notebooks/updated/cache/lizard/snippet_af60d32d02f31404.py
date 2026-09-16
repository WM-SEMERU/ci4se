def delete(name, remove=False, force=False):
    if salt.utils.data.is_true(force):
        log.warning(
            'userdel does not support force-deleting user while user is logged in'
            )
    cmd = ['userdel']
    if remove:
        cmd.append('-r')
    cmd.append(name)
    return __salt__['cmd.retcode'](cmd, python_shell=False) == 0