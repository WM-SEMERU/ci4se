def get_all_group_policies(group_name, region=None, key=None, keyid=None,
    profile=None):
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
    if not conn:
        return False
    try:
        response = conn.get_all_group_policies(group_name)
        _list = (response.list_group_policies_response.
            list_group_policies_result)
        return _list.policy_names
    except boto.exception.BotoServerError as e:
        log.debug(e)
        return []