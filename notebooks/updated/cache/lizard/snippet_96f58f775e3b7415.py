def discoverable(dev):
    if dev not in address_():
        raise CommandExecutionError(
            'Invalid dev passed to bluetooth.discoverable')
    cmd = 'hciconfig {0} iscan'.format(dev)
    __salt__['cmd.run'](cmd).splitlines()
    cmd = 'hciconfig {0}'.format(dev)
    out = __salt__['cmd.run'](cmd)
    if 'UP RUNNING ISCAN' in out:
        return True
    return False