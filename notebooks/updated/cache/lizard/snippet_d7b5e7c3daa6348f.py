def delete_key(key_name, region=None, key=None, keyid=None, profile=None):
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
    try:
        key = conn.delete_key_pair(key_name)
        log.debug('the key to return is : %s', key)
        return key
    except boto.exception.BotoServerError as e:
        log.debug(e)
        return False