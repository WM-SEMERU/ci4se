def create_tags(resource_ids, tags, region=None, key=None, keyid=None,
    profile=None):
    if not isinstance(resource_ids, list):
        resource_ids = [resource_ids]
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
    try:
        conn.create_tags(resource_ids, tags)
        return True
    except boto.exception.BotoServerError as e:
        log.error(e)
        return False