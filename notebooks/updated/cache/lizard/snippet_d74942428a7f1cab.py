def enable_api_key(apiKey, region=None, key=None, keyid=None, profile=None):
    try:
        conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
        response = _api_key_patch_replace(conn, apiKey, '/enabled', 'True')
        return {'apiKey': _convert_datetime_str(response)}
    except ClientError as e:
        return {'error': __utils__['boto3.get_error'](e)}