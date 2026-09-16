def set_(device, **kwargs):
    empty = {'block-soft-limit': 0, 'block-hard-limit': 0,
        'file-soft-limit': 0, 'file-hard-limit': 0}
    current = None
    cmd = 'setquota'
    if 'user' in kwargs:
        cmd += ' -u {0} '.format(kwargs['user'])
        parsed = _parse_quota(device, '-u')
        if kwargs['user'] in parsed:
            current = parsed['Users'][kwargs['user']]
        else:
            current = empty
        ret = 'User: {0}'.format(kwargs['user'])
    if 'group' in kwargs:
        if 'user' in kwargs:
            raise SaltInvocationError(
                'Please specify a user or group, not both.')
        cmd += ' -g {0} '.format(kwargs['group'])
        parsed = _parse_quota(device, '-g')
        if kwargs['group'] in parsed:
            current = parsed['Groups'][kwargs['group']]
        else:
            current = empty
        ret = 'Group: {0}'.format(kwargs['group'])
    if not current:
        raise CommandExecutionError('A valid user or group was not found')
    for limit in ('block-soft-limit', 'block-hard-limit', 'file-soft-limit',
        'file-hard-limit'):
        if limit in kwargs:
            current[limit] = kwargs[limit]
    cmd += '{0} {1} {2} {3} {4}'.format(current['block-soft-limit'],
        current['block-hard-limit'], current['file-soft-limit'], current[
        'file-hard-limit'], device)
    result = __salt__['cmd.run_all'](cmd, python_shell=False)
    if result['retcode'] != 0:
        raise CommandExecutionError(
            'Unable to set desired quota. Error follows: \n{0}'.format(
            result['stderr']))
    return {ret: current}