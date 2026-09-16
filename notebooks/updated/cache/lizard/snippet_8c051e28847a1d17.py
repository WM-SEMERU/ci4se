def absent(name, tags=None, region=None, key=None, keyid=None, profile=None):
    ret = {'name': name, 'result': True, 'comment': '', 'changes': {}}
    r = __salt__['boto_vpc.get_id'](name=name, tags=tags, region=region,
        key=key, keyid=keyid, profile=profile)
    if 'error' in r:
        ret['result'] = False
        ret['comment'] = 'Failed to delete VPC: {0}.'.format(r['error'][
            'message'])
        return ret
    _id = r.get('id')
    if not _id:
        ret['comment'] = '{0} VPC does not exist.'.format(name)
        return ret
    if __opts__['test']:
        ret['comment'] = 'VPC {0} is set to be removed.'.format(name)
        ret['result'] = None
        return ret
    r = __salt__['boto_vpc.delete'](vpc_name=name, tags=tags, region=region,
        key=key, keyid=keyid, profile=profile)
    if not r['deleted']:
        ret['result'] = False
        ret['comment'] = 'Failed to delete VPC: {0}.'.format(r['error'][
            'message'])
        return ret
    ret['changes']['old'] = {'vpc': _id}
    ret['changes']['new'] = {'vpc': None}
    ret['comment'] = 'VPC {0} deleted.'.format(name)
    return ret