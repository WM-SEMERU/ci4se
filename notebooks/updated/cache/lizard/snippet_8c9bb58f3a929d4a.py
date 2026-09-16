def __execute_cmd(command, host=None, admin_username=None, admin_password=
    None, module=None):
    if module:
        if module.startswith('ALL_'):
            modswitch = '-a ' + module[module.index('_') + 1:len(module)
                ].lower()
        else:
            modswitch = '-m {0}'.format(module)
    else:
        modswitch = ''
    if not host:
        cmd = __salt__['cmd.run_all']('racadm {0} {1}'.format(command,
            modswitch))
    else:
        cmd = __salt__['cmd.run_all']('racadm -r {0} -u {1} -p {2} {3} {4}'
            .format(host, admin_username, admin_password, command,
            modswitch), output_loglevel='quiet')
    if cmd['retcode'] != 0:
        log.warning('racadm returned an exit code of %s', cmd['retcode'])
        return False
    return True