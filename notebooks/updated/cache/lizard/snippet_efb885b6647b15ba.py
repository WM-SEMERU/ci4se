def absent(name, profile='grafana'):
    if isinstance(profile, string_types):
        profile = __salt__['config.option'](profile)
    ret = {'name': name, 'result': None, 'comment': None, 'changes': {}}
    user = __salt__['grafana4.get_user'](name, profile)
    if user:
        if __opts__['test']:
            ret['comment'] = 'User {0} will be deleted'.format(name)
            return ret
        orgs = __salt__['grafana4.get_user_orgs'](user['id'], profile=profile)
        __salt__['grafana4.delete_user'](user['id'], profile=profile)
        for org in orgs:
            if org['name'] == user['email']:
                __salt__['grafana4.delete_org'](org['orgId'], profile=profile)
            else:
                __salt__['grafana4.delete_user_org'](user['id'], org[
                    'orgId'], profile=profile)
    else:
        ret['result'] = True
        ret['comment'] = 'User {0} already absent'.format(name)
        return ret
    ret['result'] = True
    ret['changes'][name] = 'Absent'
    ret['comment'] = 'User {0} was deleted'.format(name)
    return ret