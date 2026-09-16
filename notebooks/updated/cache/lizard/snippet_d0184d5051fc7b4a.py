def update_function_code(FunctionName, ZipFile=None, S3Bucket=None, S3Key=
    None, S3ObjectVersion=None, Publish=False, region=None, key=None, keyid
    =None, profile=None):
    conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
    try:
        if ZipFile:
            if S3Bucket or S3Key or S3ObjectVersion:
                raise SaltInvocationError(
                    'Either ZipFile must be specified, or S3Bucket and S3Key must be provided.'
                    )
            r = conn.update_function_code(FunctionName=FunctionName,
                ZipFile=_filedata(ZipFile), Publish=Publish)
        else:
            if not S3Bucket or not S3Key:
                raise SaltInvocationError(
                    'Either ZipFile must be specified, or S3Bucket and S3Key must be provided.'
                    )
            args = {'S3Bucket': S3Bucket, 'S3Key': S3Key}
            if S3ObjectVersion:
                args['S3ObjectVersion'] = S3ObjectVersion
            r = conn.update_function_code(FunctionName=FunctionName,
                Publish=Publish, **args)
        if r:
            keys = ('FunctionName', 'Runtime', 'Role', 'Handler',
                'CodeSha256', 'CodeSize', 'Description', 'Timeout',
                'MemorySize', 'FunctionArn', 'LastModified', 'VpcConfig',
                'Environment')
            return {'updated': True, 'function': dict([(k, r.get(k)) for k in
                keys])}
        else:
            log.warning('Function was not updated')
            return {'updated': False}
    except ClientError as e:
        return {'updated': False, 'error': __utils__['boto3.get_error'](e)}