def logout(self):
    self.client.global_sign_out(AccessToken=self.access_token)
    self.id_token = None
    self.refresh_token = None
    self.access_token = None
    self.token_type = None