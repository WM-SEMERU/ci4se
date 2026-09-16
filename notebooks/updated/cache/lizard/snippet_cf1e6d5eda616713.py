def policy_definition_absent(name, connection_auth=None):
    ret = {'name': name, 'result': False, 'comment': '', 'changes': {}}
    if not isinstance(connection_auth, dict):
        ret['comment'] = (
            'Connection information must be specified via connection_auth dictionary!'
            )
        return ret
    policy = __salt__['azurearm_resource.policy_definition_get'](name,
        azurearm_log_level='info', **connection_auth)
    if 'error' in policy:
        ret['result'] = True
        ret['comment'] = 'Policy definition {0} is already absent.'.format(name
            )
        return ret
    elif __opts__['test']:
        ret['comment'] = 'Policy definition {0} would be deleted.'.format(name)
        ret['result'] = None
        ret['changes'] = {'old': policy, 'new': {}}
        return ret
    deleted = __salt__['azurearm_resource.policy_definition_delete'](name,
        **connection_auth)
    if deleted:
        ret['result'] = True
        ret['comment'] = 'Policy definition {0} has been deleted.'.format(name)
        ret['changes'] = {'old': policy, 'new': {}}
        return ret
    ret['comment'] = 'Failed to delete policy definition {0}!'.format(name)
    return ret