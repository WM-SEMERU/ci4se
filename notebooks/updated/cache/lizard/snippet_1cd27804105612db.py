def setsemod(module, state):
    if state.lower() == 'enabled':
        cmd = 'semodule -e {0}'.format(module)
    elif state.lower() == 'disabled':
        cmd = 'semodule -d {0}'.format(module)
    return not __salt__['cmd.retcode'](cmd)