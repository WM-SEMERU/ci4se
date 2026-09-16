def absent(name, region=None, key=None, keyid=None, profile=None):
    ret = {'name': name, 'result': True, 'comment': '', 'changes': {}}
    if not __salt__['boto_cfn.exists'](name, region, key, keyid, profile):
        ret['comment'] = 'Stack {0} does not exist.'.format(name)
        ret['changes'] = {}
        return ret
    if __opts__['test']:
        ret['comment'] = 'Stack {0} is set to be deleted.'.format(name)
        ret['result'] = None
        return ret
    deleted = __salt__['boto_cfn.delete'](name, region, key, keyid, profile)
    if isinstance(deleted, six.string_types):
        code, message = _get_error(deleted)
        ret['comment'] = 'Stack {0} could not be deleted.\n{1}\n{2}'.format(
            name, code, message)
        ret['result'] = False
        ret['changes'] = {}
        return ret
    if deleted:
        ret['comment'] = 'Stack {0} was deleted.'.format(name)
        ret['changes']['deleted'] = name
        return ret