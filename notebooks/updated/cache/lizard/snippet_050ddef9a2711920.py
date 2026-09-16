def list_users(host=None, admin_username=None, admin_password=None, module=None
    ):
    users = {}
    _username = ''
    for idx in range(1, 17):
        cmd = __execute_ret('getconfig -g cfgUserAdmin -i {0}'.format(idx),
            host=host, admin_username=admin_username, admin_password=
            admin_password)
        if cmd['retcode'] != 0:
            log.warning('racadm returned an exit code of %s', cmd['retcode'])
        for user in cmd['stdout'].splitlines():
            if not user.startswith('cfg'):
                continue
            key, val = user.split('=')
            if key.startswith('cfgUserAdminUserName'):
                _username = val.strip()
                if val:
                    users[_username] = {'index': idx}
                else:
                    break
            elif _username:
                users[_username].update({key: val})
    return users