def upload(host, user, local_dir, remote_dir, rsync_options=RSYNC_OPTIONS):
    if user is None:
        user = ''
    else:
        user = user + '@'
    if host is None or host == 'localhost':
        host = ''
    else:
        host = host + ':'
    if not local_dir.endswith('/'):
        local_dir = local_dir + '/'
    if not remote_dir.endswith('/'):
        remote_dir = remote_dir + '/'
    remote_string = '{user}{host}{remote_dir}'.format(**locals())
    cmds = ['rsync']
    cmds += shlex.split(rsync_options)
    cmds += [local_dir, remote_string]
    run(cmds)
    return [remote_string]