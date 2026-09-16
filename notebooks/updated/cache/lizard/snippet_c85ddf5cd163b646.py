def absent(email, profile='splunk', **kwargs):
    user_identity = kwargs.get('name')
    ret = {'name': user_identity, 'changes': {}, 'result': None, 'comment':
        'User {0} is absent.'.format(user_identity)}
    target = __salt__['splunk.get_user'](email, profile=profile)
    if not target:
        ret['comment'] = 'User {0} does not exist'.format(user_identity)
        ret['result'] = True
        return ret
    if __opts__['test']:
        ret['comment'] = 'User {0} is all set to be deleted'.format(
            user_identity)
        ret['result'] = None
        return ret
    result = __salt__['splunk.delete_user'](email, profile=profile)
    if result:
        ret['comment'] = 'Deleted user {0}'.format(user_identity)
        ret['changes'].setdefault('old', 'User {0} exists'.format(
            user_identity))
        ret['changes'].setdefault('new', 'User {0} deleted'.format(
            user_identity))
        ret['result'] = True
    else:
        ret['comment'] = 'Failed to delete {0}'.format(user_identity)
        ret['result'] = False
    return ret