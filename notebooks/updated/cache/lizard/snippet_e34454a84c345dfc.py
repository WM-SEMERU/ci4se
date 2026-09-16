def stop(name):
    if _service_is_upstart(name):
        cmd = 'stop {0}'.format(name)
    else:
        cmd = '/sbin/service {0} stop'.format(name)
    return not __salt__['cmd.retcode'](cmd, python_shell=False)