def start(name):
    if _service_is_upstart(name):
        cmd = 'start {0}'.format(name)
    else:
        cmd = '/sbin/service {0} start'.format(name)
    return not __salt__['cmd.retcode'](cmd, python_shell=False)