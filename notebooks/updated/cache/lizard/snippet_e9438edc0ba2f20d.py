def hosted_zone_absent(name, domain_name=None, region=None, key=None, keyid
    =None, profile=None):
    domain_name = domain_name if domain_name else name
    ret = {'name': name, 'result': True, 'comment': '', 'changes': {}}
    deets = __salt__['boto_route53.describe_hosted_zones'](domain_name=
        domain_name, region=region, key=key, keyid=keyid, profile=profile)
    if not deets:
        ret['comment'] = 'Hosted Zone {0} already absent'.format(domain_name)
        log.info(ret['comment'])
        return ret
    if __opts__['test']:
        ret['comment'] = 'Route53 Hosted Zone {0} set to be deleted.'.format(
            domain_name)
        ret['result'] = None
        return ret
    if __salt__['boto_route53.delete_zone'](zone=domain_name, region=region,
        key=key, keyid=keyid, profile=profile):
        ret['comment'] = 'Route53 Hosted Zone {0} deleted'.format(domain_name)
        log.info(ret['comment'])
        ret['changes']['old'] = deets
        ret['changes']['new'] = None
    return ret