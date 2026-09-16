def off(device):
    cmd = 'quotaoff {0}'.format(device)
    __salt__['cmd.run'](cmd, python_shell=False)
    return True