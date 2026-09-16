def delete(name, region=None, key=None, keyid=None, profile=None):
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
    conn.delete_topic(get_arn(name, region, key, keyid, profile))
    log.info('Deleted SNS topic %s', name)
    _invalidate_cache()
    return True