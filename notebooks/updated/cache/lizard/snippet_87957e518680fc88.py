def _set(self, value):
    user = self.USER
    try:
        uid = pwd.getpwnam(user).pw_uid
    except KeyError:
        log.info('User does not exist')
        result = {}
        result['retcode'] = 1
        result['stdout'] = 'User {0} does not exist'.format(user)
        return result
    cmd = self.gsetting_command + ['set', self.SCHEMA, self.KEY, value]
    environ = {}
    environ['XDG_RUNTIME_DIR'] = '/run/user/{0}'.format(uid)
    result = __salt__['cmd.run_all'](cmd, runas=user, env=environ,
        python_shell=False)
    return result