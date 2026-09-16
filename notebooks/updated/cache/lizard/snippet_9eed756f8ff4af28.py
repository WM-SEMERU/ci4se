def status(name, sig=None):
    if sig:
        return bool(__salt__['status.pid'](sig))
    cmd = '{0} check {1}'.format(_cmd(), name)
    return not __salt__['cmd.retcode'](cmd)