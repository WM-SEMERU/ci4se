def restart(name):
    if _service_is_upstart(name):
        cmd = 'restart {0}'.format(name)
    else:
        cmd = '/sbin/service {0} restart'.format(name)
    return not __salt__['cmd.retcode'](cmd, python_shell=False)