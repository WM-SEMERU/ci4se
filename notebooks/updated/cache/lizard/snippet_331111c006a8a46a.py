def authorize_client_credentials(self, client_id, client_secret=None, scope
    ='private_agent'):
    self.auth_data = {'grant_type': 'client_credentials', 'scope': [scope],
        'client_id': client_id, 'client_secret': client_secret}
    self._do_authorize()