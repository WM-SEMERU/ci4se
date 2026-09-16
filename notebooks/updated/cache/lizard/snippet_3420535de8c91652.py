def create(name, description, vpc_id=None, vpc_name=None, region=None, key=
    None, keyid=None, profile=None):
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
    if not vpc_id and vpc_name:
        try:
            vpc_id = _vpc_name_to_id(vpc_id=vpc_id, vpc_name=vpc_name,
                region=region, key=key, keyid=keyid, profile=profile)
        except boto.exception.BotoServerError as e:
            log.debug(e)
            return False
    created = conn.create_security_group(name, description, vpc_id)
    if created:
        log.info('Created security group %s.', name)
        return True
    else:
        msg = 'Failed to create security group {0}.'.format(name)
        log.error(msg)
        return False