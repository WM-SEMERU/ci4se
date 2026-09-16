def activated(name, path, user):
    ret = {'name': name, 'changes': {}, 'comment': '', 'result': False}
    check = __salt__['wordpress.show_plugin'](name, path, user)
    if check['status'] == 'active':
        ret['result'] = True
        ret['comment'] = 'Plugin already activated: {0}'.format(name)
        return ret
    elif __opts__['test']:
        ret['result'] = None
        ret['comment'] = 'Plugin will be activated: {0}'.format(name)
        return ret
    resp = __salt__['wordpress.activate'](name, path, user)
    if resp is True:
        ret['result'] = True
        ret['comment'] = 'Plugin activated: {0}'.format(name)
        ret['changes'] = {'old': check, 'new': __salt__[
            'wordpress.show_plugin'](name, path, user)}
    elif resp is None:
        ret['result'] = True
        ret['comment'] = 'Plugin already activated: {0}'.format(name)
        ret['changes'] = {'old': check, 'new': __salt__[
            'wordpress.show_plugin'](name, path, user)}
    else:
        ret['comment'] = 'Plugin failed to activate: {0}'.format(name)
    return ret