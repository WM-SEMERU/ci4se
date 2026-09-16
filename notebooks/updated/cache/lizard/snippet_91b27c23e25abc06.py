def validate_verification(self, confirmation_code, attribute='email'):
    self.check_token()
    return self.client.verify_user_attribute(AccessToken=self.access_token,
        AttributeName=attribute, Code=confirmation_code)