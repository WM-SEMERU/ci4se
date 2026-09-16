def volume_attached(name, server_name, provider=None, **kwargs):
    ret = _check_name(name)
    if not ret['result']:
        return ret
    ret = _check_name(server_name)
    if not ret['result']:
        return ret
    volumes = __salt__['cloud.volume_list'](provider=provider)
    instance = __salt__['cloud.action'](fun='show_instance', names=server_name)
    if name in volumes and volumes[name]['attachments']:
        volume = volumes[name]
        ret['comment'
            ] = 'Volume {name} is already attached: {attachments}'.format(**
            volumes[name])
        ret['result'] = True
        return ret
    elif name not in volumes:
        ret['comment'] = 'Volume {0} does not exist'.format(name)
        ret['result'] = False
        return ret
    elif not instance:
        ret['comment'] = 'Server {0} does not exist'.format(server_name)
        ret['result'] = False
        return ret
    elif __opts__['test']:
        ret['comment'] = 'Volume {0} will be will be attached.'.format(name)
        ret['result'] = None
        return ret
    response = __salt__['cloud.volume_attach'](provider=provider, names=
        name, server_name=server_name, **kwargs)
    if response:
        ret['result'] = True
        ret['comment'] = 'Volume {0} was created'.format(name)
        ret['changes'] = {'old': volumes[name], 'new': response}
    else:
        ret['result'] = False
        ret['comment'] = 'Volume {0} failed to attach.'.format(name)
    return ret