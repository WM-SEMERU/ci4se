def build_policy(region=None, key=None, keyid=None, profile=None):
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
    if hasattr(conn, 'build_policy'):
        policy = salt.utils.json.loads(conn.build_policy())
    elif hasattr(conn, '_build_policy'):
        policy = salt.utils.json.loads(conn._build_policy())
    else:
        return {}
    for key, policy_val in policy.items():
        for statement in policy_val:
            if isinstance(statement['Action'], list) and len(statement[
                'Action']) == 1:
                statement['Action'] = statement['Action'][0]
            if isinstance(statement['Principal']['Service'], list) and len(
                statement['Principal']['Service']) == 1:
                statement['Principal']['Service'] = statement['Principal'][
                    'Service'][0]
    policy['Version'] = '2008-10-17'
    return policy