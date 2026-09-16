def delete_option_group(name, region=None, key=None, keyid=None, profile=None):
    try:
        conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
        if not conn:
            return {'deleted': bool(conn)}
        res = conn.delete_option_group(OptionGroupName=name)
        if not res:
            return {'deleted': bool(res), 'message':
                'Failed to delete RDS option group {0}.'.format(name)}
        return {'deleted': bool(res), 'message':
            'Deleted RDS option group {0}.'.format(name)}
    except ClientError as e:
        return {'error': __utils__['boto3.get_error'](e)}