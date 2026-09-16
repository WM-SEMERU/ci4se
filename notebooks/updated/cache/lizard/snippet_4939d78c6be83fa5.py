def coalesce(name, **kwargs):
    ret = {'name': name, 'changes': {}, 'result': True, 'comment':
        'Network device {0} coalescing settings are up to date.'.format(name)}
    apply_coalescing = False
    if 'test' not in kwargs:
        kwargs['test'] = __opts__.get('test', False)
    try:
        old = __salt__['ethtool.show_coalesce'](name)
        if not isinstance(old, dict):
            ret['result'] = False
            ret['comment'
                ] = 'Device {0} coalescing settings are not supported'.format(
                name)
            return ret
        new = {}
        diff = []
        for key, value in kwargs.items():
            if key in old and value != old[key]:
                new.update({key: value})
                diff.append('{0}: {1}'.format(key, value))
        if kwargs['test']:
            if not new:
                return ret
            if new:
                ret['result'] = None
                ret['comment'] = (
                    'Device {0} coalescing settings are set to be updated:\n{1}'
                    .format(name, '\n'.join(diff)))
                return ret
        if new:
            apply_coalescing = True
            ret['comment'] = 'Device {0} coalescing settings updated.'.format(
                name)
            ret['changes']['ethtool_coalesce'] = '\n'.join(diff)
    except AttributeError as error:
        ret['result'] = False
        ret['comment'] = six.text_type(error)
        return ret
    if apply_coalescing:
        try:
            __salt__['ethtool.set_coalesce'](name, **new)
        except AttributeError as error:
            ret['result'] = False
            ret['comment'] = six.text_type(error)
            return ret
    return ret