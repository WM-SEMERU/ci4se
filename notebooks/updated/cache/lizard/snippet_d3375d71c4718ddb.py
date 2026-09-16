def with_mfa(self, mfa_token):
    if hasattr(mfa_token, '__call__'):
        self.context.mfa_token = mfa_token.__call__()
    else:
        self.context.mfa_token = mfa_token
    return self