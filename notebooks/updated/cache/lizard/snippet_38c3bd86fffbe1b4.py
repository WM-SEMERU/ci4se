def make_application_private(application_id, sar_client=None):
    if not application_id:
        raise ValueError('Require application id to make the app private')
    if not sar_client:
        sar_client = boto3.client('serverlessrepo')
    sar_client.put_application_policy(ApplicationId=application_id,
        Statements=[])