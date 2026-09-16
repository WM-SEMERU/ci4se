def get_authorization_url(self):
    return self._build_authorization_request_url(response_type=auth.
        CODE_RESPONSE_TYPE, redirect_url=self.redirect_url, state=self.
        state_token)