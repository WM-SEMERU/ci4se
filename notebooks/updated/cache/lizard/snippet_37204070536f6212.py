def read(domain, key, user=None):
    cmd = 'defaults read "{0}" "{1}"'.format(domain, key)
    return __salt__['cmd.run'](cmd, runas=user)