def create_app(name, site, sourcepath, apppool=None):
    ret = {'name': name, 'changes': {}, 'comment': str(), 'result': None}
    current_apps = __salt__['win_iis.list_apps'](site)
    if name in current_apps:
        ret['comment'] = 'Application already present: {0}'.format(name)
        ret['result'] = True
    elif __opts__['test']:
        ret['comment'] = 'Application will be created: {0}'.format(name)
        ret['changes'] = {'old': None, 'new': name}
    else:
        ret['comment'] = 'Created application: {0}'.format(name)
        ret['changes'] = {'old': None, 'new': name}
        ret['result'] = __salt__['win_iis.create_app'](name, site,
            sourcepath, apppool)
    return ret