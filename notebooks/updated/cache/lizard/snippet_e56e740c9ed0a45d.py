def init(runlevel):
    cmd = ['init', '{0}'.format(runlevel)]
    ret = __salt__['cmd.run'](cmd, python_shell=False)
    return ret