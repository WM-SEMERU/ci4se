def verify_token_type(self):
    try:
        token_type = self.payload[api_settings.TOKEN_TYPE_CLAIM]
    except KeyError:
        raise TokenError(_('Token has no type'))
    if self.token_type != token_type:
        raise TokenError(_('Token has wrong type'))