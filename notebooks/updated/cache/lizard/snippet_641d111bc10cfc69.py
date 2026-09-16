def client_validate_password(self, client, password):
    client = self._client_id(client)
    body = {'action': 'validate_password', 'auth_password': password}
    response = self._put(url.clients_id.format(id=client), body=body)
    self._check_response(response, 200)