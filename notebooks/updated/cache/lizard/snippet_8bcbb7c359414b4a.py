def connect_service(service, credentials, region_name=None, config=None,
    silent=False):
    api_client = None
    try:
        client_params = {}
        client_params['service_name'] = service.lower()
        session_params = {}
        session_params['aws_access_key_id'] = credentials['AccessKeyId']
        session_params['aws_secret_access_key'] = credentials['SecretAccessKey'
            ]
        session_params['aws_session_token'] = credentials['SessionToken']
        if region_name:
            client_params['region_name'] = region_name
            session_params['region_name'] = region_name
        if config:
            client_params['config'] = config
        aws_session = boto3.session.Session(**session_params)
        if not silent:
            infoMessage = 'Connecting to AWS %s' % service
            if region_name:
                infoMessage = infoMessage + ' in %s' % region_name
            printInfo('%s...' % infoMessage)
        api_client = aws_session.client(**client_params)
    except Exception as e:
        printException(e)
    return api_client