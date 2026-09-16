def delete(self, username, napp):
    api = self._config.get('napps', 'api')
    endpoint = os.path.join(api, 'napps', username, napp, '')
    content = {'token': self._config.get('auth', 'token')}
    response = self.make_request(endpoint, json=content, method='DELETE')
    response.raise_for_status()