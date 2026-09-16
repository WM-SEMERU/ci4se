def group_exists(name, region=None, key=None, keyid=None, profile=None):
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
    try:
        conn.describe_replication_groups(name)
        return True
    except boto.exception.BotoServerError as e:
        log.debug(e)
        return False