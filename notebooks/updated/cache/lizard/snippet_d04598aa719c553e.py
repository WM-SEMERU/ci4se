def absent(name, zone, record_type, identifier=None, region=None, key=None,
    keyid=None, profile=None, wait_for_sync=True, split_dns=False,
    private_zone=False):
    ret = {'name': name, 'result': True, 'comment': '', 'changes': {}}
    record = __salt__['boto_route53.get_record'](name, zone, record_type,
        False, region, key, keyid, profile, split_dns, private_zone, identifier
        )
    if record:
        if __opts__['test']:
            ret['comment'] = 'Route53 record {0} set to be deleted.'.format(
                name)
            ret['result'] = None
            return ret
        deleted = __salt__['boto_route53.delete_record'](name, zone,
            record_type, identifier, False, region, key, keyid, profile,
            wait_for_sync, split_dns, private_zone)
        if deleted:
            ret['changes']['old'] = record
            ret['changes']['new'] = None
            ret['comment'] = 'Deleted {0} Route53 record.'.format(name)
        else:
            ret['result'] = False
            ret['comment'] = 'Failed to delete {0} Route53 record.'.format(name
                )
    else:
        ret['comment'] = '{0} does not exist.'.format(name)
    return ret