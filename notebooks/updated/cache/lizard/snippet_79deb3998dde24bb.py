def describe_api_model(restApiId, modelName, flatten=True, region=None, key
    =None, keyid=None, profile=None):
    try:
        conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
        model = conn.get_model(restApiId=restApiId, modelName=modelName,
            flatten=flatten)
        return {'model': _convert_datetime_str(model)}
    except ClientError as e:
        return {'error': __utils__['boto3.get_error'](e)}