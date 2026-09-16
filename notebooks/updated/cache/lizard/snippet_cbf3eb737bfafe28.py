def vmotion_configured(name, enabled, device='vmk0'):
    ret = {'name': name, 'result': False, 'changes': {}, 'comment': ''}
    esxi_cmd = 'esxi.cmd'
    host = __pillar__['proxy']['host']
    current_vmotion_enabled = __salt__[esxi_cmd]('get_vmotion_enabled').get(
        host)
    current_vmotion_enabled = current_vmotion_enabled.get('VMotion Enabled')
    if enabled != current_vmotion_enabled:
        if not __opts__['test']:
            if enabled is True:
                response = __salt__[esxi_cmd]('vmotion_enable', device=device
                    ).get(host)
                error = response.get('Error')
                if error:
                    ret['comment'] = 'Error: {0}'.format(error)
                    return ret
            else:
                response = __salt__[esxi_cmd]('vmotion_disable').get(host)
                error = response.get('Error')
                if error:
                    ret['comment'] = 'Error: {0}'.format(error)
                    return ret
        ret['changes'].update({'enabled': {'old': current_vmotion_enabled,
            'new': enabled}})
    ret['result'] = True
    if ret['changes'] == {}:
        ret['comment'
            ] = 'VMotion configuration is already in the desired state.'
        return ret
    if __opts__['test']:
        ret['result'] = None
        ret['comment'] = 'VMotion configuration will change.'
    return ret