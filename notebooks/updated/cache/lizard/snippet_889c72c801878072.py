def process(self, request, response, environ):
    token_data = self.token_generator.create_access_token_data(self.
        refresh_grant_type)
    expires_at = int(time.time()) + token_data['expires_in']
    access_token = AccessToken(client_id=self.client.identifier, token=
        token_data['access_token'], grant_type=self.refresh_grant_type,
        data=self.data, expires_at=expires_at, scopes=self.scope_handler.
        scopes, user_id=self.user_id)
    if self.reissue_refresh_tokens:
        self.access_token_store.delete_refresh_token(self.refresh_token)
        access_token.refresh_token = token_data['refresh_token']
        refresh_expires_in = self.token_generator.refresh_expires_in
        refresh_expires_at = int(time.time()) + refresh_expires_in
        access_token.refresh_expires_at = refresh_expires_at
    else:
        del token_data['refresh_token']
    self.access_token_store.save_token(access_token)
    json_success_response(data=token_data, response=response)
    return response