def get_aws_creds(self):
    result = {}
    if boto3.DEFAULT_SESSION:
        session = boto3.DEFAULT_SESSION
    else:
        session = boto3.session.Session()
    profile_name = session.profile_name if session else None
    LOG.debug("Loading AWS credentials from session with profile '%s'",
        profile_name)
    if not session:
        return result
    creds = session.get_credentials()
    if not creds:
        return result
    if hasattr(session, 'region_name') and session.region_name:
        result['region'] = session.region_name
    if hasattr(creds, 'access_key') and creds.access_key:
        result['key'] = creds.access_key
    if hasattr(creds, 'secret_key') and creds.secret_key:
        result['secret'] = creds.secret_key
    if hasattr(creds, 'token') and creds.token:
        result['sessiontoken'] = creds.token
    return result