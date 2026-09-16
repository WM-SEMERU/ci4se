def create_alias(FunctionName, Name, FunctionVersion, Description='',
    region=None, key=None, keyid=None, profile=None):
    try:
        conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
        alias = conn.create_alias(FunctionName=FunctionName, Name=Name,
            FunctionVersion=FunctionVersion, Description=Description)
        if alias:
            log.info('The newly created alias name is %s', alias['Name'])
            return {'created': True, 'name': alias['Name']}
        else:
            log.warning('Alias was not created')
            return {'created': False}
    except ClientError as e:
        return {'created': False, 'error': __utils__['boto3.get_error'](e)}