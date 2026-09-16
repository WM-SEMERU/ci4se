def configureIAMCredentials(self, AWSAccessKeyID, AWSSecretAccessKey,
    AWSSessionToken=''):
    iam_credentials_provider = IAMCredentialsProvider()
    iam_credentials_provider.set_access_key_id(AWSAccessKeyID)
    iam_credentials_provider.set_secret_access_key(AWSSecretAccessKey)
    iam_credentials_provider.set_session_token(AWSSessionToken)
    self._mqtt_core.configure_iam_credentials(iam_credentials_provider)