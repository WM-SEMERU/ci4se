def attached(name, force=False):
    ret = {'name': name, 'changes': {}, 'result': None, 'comment': ''}
    zones = __salt__['zoneadm.list'](installed=True, configured=True)
    if name in zones:
        if zones[name]['state'] == 'configured':
            if __opts__['test']:
                res_attach = {'status': True}
            else:
                res_attach = __salt__['zoneadm.attach'](name, force)
            ret['result'] = res_attach['status']
            if ret['result']:
                ret['changes'][name] = 'attached'
                ret['comment'] = 'The zone {0} was attached.'.format(name)
            else:
                ret['comment'] = []
                ret['comment'].append('Failed to attach zone {0}!'.format(name)
                    )
                if 'message' in res_attach:
                    ret['comment'].append(res_attach['message'])
                ret['comment'] = '\n'.join(ret['comment'])
        else:
            ret['result'] = True
            ret['comment'] = 'zone {0} already attached.'.format(name)
    else:
        ret['result'] = False
        ret['comment'] = 'zone {0} is not configured!'.format(name)
    return ret