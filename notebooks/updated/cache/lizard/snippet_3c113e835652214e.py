def installed(name, nodataset=False, brand_opts=None):
    ret = {'name': name, 'changes': {}, 'result': None, 'comment': ''}
    zones = __salt__['zoneadm.list'](installed=True, configured=True)
    if name in zones:
        if zones[name]['state'] == 'configured':
            if __opts__['test']:
                res_install = {'status': True}
            else:
                res_install = __salt__['zoneadm.install'](name, nodataset,
                    brand_opts)
            ret['result'] = res_install['status']
            if ret['result']:
                ret['changes'][name] = 'installed'
                ret['comment'] = 'The zone {0} was installed.'.format(name)
            else:
                ret['comment'] = []
                ret['comment'].append('Failed to install zone {0}!'.format(
                    name))
                if 'message' in res_install:
                    ret['comment'].append(res_install['message'])
                ret['comment'] = '\n'.join(ret['comment'])
        else:
            ret['result'] = True
            ret['comment'] = 'zone {0} already installed.'.format(name)
    else:
        ret['result'] = False
        ret['comment'] = 'zone {0} is not configured!'.format(name)
    return ret