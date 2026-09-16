def function_exists(FunctionName, region=None, key=None, keyid=None,
    profile=None):
    try:
        func = _find_function(FunctionName, region=region, key=key, keyid=
            keyid, profile=profile)
        return {'exists': bool(func)}
    except ClientError as e:
        return {'error': __utils__['boto3.get_error'](e)}