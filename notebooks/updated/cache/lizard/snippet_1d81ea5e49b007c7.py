def peer(name):
    if salt.utils.cloud.check_name(name, 'a-zA-Z0-9._-'):
        raise SaltInvocationError('Invalid characters in peer name "{0}"'.
            format(name))
    cmd = 'peer probe {0}'.format(name)
    return _gluster(cmd)