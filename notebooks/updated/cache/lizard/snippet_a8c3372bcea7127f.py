def _find_identity_pool_ids(name, pool_id, conn):
    ids = []
    if pool_id is None:
        for pools in __utils__['boto3.paged_call'](conn.list_identity_pools,
            marker_flag='NextToken', marker_arg='NextToken', MaxResults=25):
            for pool in pools['IdentityPools']:
                if pool['IdentityPoolName'] == name:
                    ids.append(pool['IdentityPoolId'])
    else:
        ids.append(pool_id)
    return ids