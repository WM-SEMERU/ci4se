def access_token_response_data(self, access_token, response_type=None, nonce=''
    ):
    scope = constants.DEFAULT_SCOPE
    extra_data = {}
    if provider.scope.check(constants.OPEN_ID_SCOPE, access_token.scope):
        id_token = self.get_id_token(access_token, nonce)
        extra_data['id_token'] = self.encode_id_token(id_token)
        scope = provider.scope.to_int(*id_token.scopes)
    access_token.scope = scope
    access_token.save()
    response_data = super(AccessTokenView, self).access_token_response_data(
        access_token)
    response_data = dict(extra_data.items() + response_data.items())
    return response_data