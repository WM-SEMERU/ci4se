def get_offset():
    if 'AIX' not in __grains__['os_family']:
        return __salt__['cmd.run'](['date', '+%z'], python_shell=False)
    salt_path = '/opt/salt/bin/date'
    if not os.path.exists(salt_path):
        return 'date in salt binaries does not exist: {0}'.format(salt_path)
    return __salt__['cmd.run']([salt_path, '+%z'], python_shell=False)