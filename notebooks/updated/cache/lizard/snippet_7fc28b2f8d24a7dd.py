def syslog(server, enable=True, host=None, admin_username=None,
    admin_password=None, module=None):
    if enable and __execute_cmd(
        'config -g cfgRemoteHosts -o cfgRhostsSyslogEnable 1', host=host,
        admin_username=admin_username, admin_password=admin_password,
        module=None):
        return __execute_cmd(
            'config -g cfgRemoteHosts -o cfgRhostsSyslogServer1 {0}'.format
            (server), host=host, admin_username=admin_username,
            admin_password=admin_password, module=module)
    return __execute_cmd('config -g cfgRemoteHosts -o cfgRhostsSyslogEnable 0',
        host=host, admin_username=admin_username, admin_password=
        admin_password, module=module)