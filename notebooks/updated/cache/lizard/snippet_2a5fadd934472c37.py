def absent(name, user=None, config=None):
    ret = {'name': name, 'changes': {}, 'result': True, 'comment': ''}
    if not user:
        config = config or '/etc/ssh/ssh_known_hosts'
    else:
        config = config or '.ssh/known_hosts'
    if not user and not os.path.isabs(config):
        comment = 'If not specifying a "user", specify an absolute "config".'
        ret['result'] = False
        return dict(ret, comment=comment)
    known_host = __salt__['ssh.get_known_host_entries'](user=user, hostname
        =name, config=config)
    if not known_host:
        return dict(ret, comment='Host is already absent')
    if __opts__['test']:
        comment = 'Key for {0} is set to be removed from {1}'.format(name,
            config)
        ret['result'] = None
        return dict(ret, comment=comment)
    rm_result = __salt__['ssh.rm_known_host'](user=user, hostname=name,
        config=config)
    if rm_result['status'] == 'error':
        return dict(ret, result=False, comment=rm_result['error'])
    else:
        return dict(ret, changes={'old': known_host, 'new': None}, result=
            True, comment=rm_result['comment'])