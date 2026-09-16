def fetch_password_policy(self, credentials):
    self.fetchstatuslogger.counts['password_policy']['discovered'] = 0
    self.fetchstatuslogger.counts['password_policy']['fetched'] = 0
    try:
        api_client = connect_service('iam', credentials, silent=True)
        self.password_policy = api_client.get_account_password_policy()[
            'PasswordPolicy']
        if 'PasswordReusePrevention' not in self.password_policy:
            self.password_policy['PasswordReusePrevention'] = False
        else:
            self.password_policy['PreviousPasswordPrevented'
                ] = self.password_policy['PasswordReusePrevention']
            self.password_policy['PasswordReusePrevention'] = True
        if 'MaxPasswordAge' in self.password_policy:
            self.password_policy['ExpirePasswords'] = True
        self.fetchstatuslogger.counts['password_policy']['discovered'] = 1
        self.fetchstatuslogger.counts['password_policy']['fetched'] = 1
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchEntity':
            self.password_policy = {}
            self.password_policy['MinimumPasswordLength'] = '1'
            self.password_policy['RequireUppercaseCharacters'] = False
            self.password_policy['RequireLowercaseCharacters'] = False
            self.password_policy['RequireNumbers'] = False
            self.password_policy['RequireSymbols'] = False
            self.password_policy['PasswordReusePrevention'] = False
            self.password_policy['ExpirePasswords'] = False
        else:
            raise e
    except Exception as e:
        printError(str(e))