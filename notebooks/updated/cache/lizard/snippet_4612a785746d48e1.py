def optionsFromEnvironment(defaults=None):
    options = defaults or {}
    credentials = options.get('credentials', {})
    rootUrl = os.environ.get('TASKCLUSTER_ROOT_URL')
    if rootUrl:
        options['rootUrl'] = rootUrl
    clientId = os.environ.get('TASKCLUSTER_CLIENT_ID')
    if clientId:
        credentials['clientId'] = clientId
    accessToken = os.environ.get('TASKCLUSTER_ACCESS_TOKEN')
    if accessToken:
        credentials['accessToken'] = accessToken
    certificate = os.environ.get('TASKCLUSTER_CERTIFICATE')
    if certificate:
        credentials['certificate'] = certificate
    if credentials:
        options['credentials'] = credentials
    return options