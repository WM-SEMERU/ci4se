def share_application_with_accounts(application_id, account_ids, sar_client
    =None):
    if not application_id or not account_ids:
        raise ValueError(
            'Require application id and list of AWS account IDs to share the app'
            )
    if not sar_client:
        sar_client = boto3.client('serverlessrepo')
    application_policy = ApplicationPolicy(account_ids, [ApplicationPolicy.
        DEPLOY])
    application_policy.validate()
    sar_client.put_application_policy(ApplicationId=application_id,
        Statements=[application_policy.to_statement()])