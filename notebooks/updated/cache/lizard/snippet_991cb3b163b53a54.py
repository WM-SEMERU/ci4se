def cognito_idp_user_pool_arn(self, lookup, default=None):
    client = EFAwsResolver.__CLIENTS['cognito-idp']
    user_pool_id = self.cognito_idp_user_pool_id(lookup, default)
    if user_pool_id == default:
        return default
    response = client.describe_user_pool(UserPoolId=user_pool_id)
    if not response.has_key('UserPool'):
        return default
    return response['UserPool']['Arn']