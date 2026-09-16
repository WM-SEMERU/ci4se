def subnet_group_exists(name, tags=None, region=None, key=None, keyid=None,
    profile=None):
    try:
        conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
        if not conn:
            return {'exists': bool(conn)}
        rds = conn.describe_db_subnet_groups(DBSubnetGroupName=name)
        return {'exists': bool(rds)}
    except ClientError as e:
        if 'DBSubnetGroupNotFoundFault' in e.message:
            return {'exists': False}
        else:
            return {'error': __utils__['boto3.get_error'](e)}