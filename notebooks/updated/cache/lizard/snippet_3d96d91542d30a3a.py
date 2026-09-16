def set_management_icmp(enabled=True, deploy=False):
    if enabled is True:
        value = 'no'
    elif enabled is False:
        value = 'yes'
    else:
        raise CommandExecutionError(
            'Invalid option provided for service enabled option.')
    ret = {}
    query = {'type': 'config', 'action': 'set', 'xpath':
        "/config/devices/entry[@name='localhost.localdomain']/deviceconfig/system/service"
        , 'element': '<disable-icmp>{0}</disable-icmp>'.format(value)}
    ret.update(__proxy__['panos.call'](query))
    if deploy is True:
        ret.update(commit())
    return ret