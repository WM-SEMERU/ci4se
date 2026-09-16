def delete_group_policy(group_name, policy_name, region=None, key=None,
    keyid=None, profile=None):
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
    if not conn:
        return False
    _policy = get_group_policy(group_name, policy_name, region, key, keyid,
        profile)
    if not _policy:
        return True
    try:
        conn.delete_group_policy(group_name, policy_name)
        log.info('Successfully deleted policy %s for IAM group %s.',
            policy_name, group_name)
        return True
    except boto.exception.BotoServerError as e:
        log.debug(e)
        log.error('Failed to delete policy %s for IAM group %s.',
            policy_name, group_name)
        return False