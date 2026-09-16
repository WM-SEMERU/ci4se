def policy_exists(policy_name, region=None, key=None, keyid=None, profile=None
    ):
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
    try:
        conn.get_policy(_get_policy_arn(policy_name, region=region, key=key,
            keyid=keyid, profile=profile))
        return True
    except boto.exception.BotoServerError:
        return False