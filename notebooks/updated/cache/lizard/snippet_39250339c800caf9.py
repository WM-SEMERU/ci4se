def get_role_policy(role_name, policy_name, region=None, key=None, keyid=
    None, profile=None):
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
    try:
        _policy = conn.get_role_policy(role_name, policy_name)
        _policy = _policy.get_role_policy_response.policy_document
        _policy = _unquote(_policy)
        _policy = salt.utils.json.loads(_policy, object_pairs_hook=odict.
            OrderedDict)
        return _policy
    except boto.exception.BotoServerError:
        return {}