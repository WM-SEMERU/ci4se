def absent(name, Name, region=None, key=None, keyid=None, profile=None):
    ret = {'name': Name, 'result': True, 'comment': '', 'changes': {}}
    r = __salt__['boto_cloudtrail.exists'](Name, region=region, key=key,
        keyid=keyid, profile=profile)
    if 'error' in r:
        ret['result'] = False
        ret['comment'] = 'Failed to delete trail: {0}.'.format(r['error'][
            'message'])
        return ret
    if r and not r['exists']:
        ret['comment'] = 'CloudTrail {0} does not exist.'.format(Name)
        return ret
    if __opts__['test']:
        ret['comment'] = 'CloudTrail {0} is set to be removed.'.format(Name)
        ret['result'] = None
        return ret
    r = __salt__['boto_cloudtrail.delete'](Name, region=region, key=key,
        keyid=keyid, profile=profile)
    if not r['deleted']:
        ret['result'] = False
        ret['comment'] = 'Failed to delete trail: {0}.'.format(r['error'][
            'message'])
        return ret
    ret['changes']['old'] = {'trail': Name}
    ret['changes']['new'] = {'trail': None}
    ret['comment'] = 'CloudTrail {0} deleted.'.format(Name)
    return ret