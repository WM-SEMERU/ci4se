def restorecon(path, recursive=False):
    if recursive:
        cmd = ['restorecon', '-FR', path]
    else:
        cmd = ['restorecon', '-F', path]
    return not __salt__['cmd.retcode'](cmd, python_shell=False)