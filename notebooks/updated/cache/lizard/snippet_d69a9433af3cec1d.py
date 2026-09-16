def describe_api_keys(region=None, key=None, keyid=None, profile=None):
    try:
        conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
        apikeys = _multi_call(conn.get_api_keys, 'items')
        return {'apiKeys': [_convert_datetime_str(apikey) for apikey in
            apikeys]}
    except ClientError as e:
        return {'error': __utils__['boto3.get_error'](e)}