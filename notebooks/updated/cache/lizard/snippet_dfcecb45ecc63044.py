def refresh(self):
    params = {'grant_type': 'refresh_token', 'refresh_token': self.
        refresh_token}
    response = self._post('oauth', 'token', params=params)
    response = self._handle_response(response)
    blob = response.json()
    self.access_token = blob.get('access_token', None)
    self.refresh_token = blob.get('refresh_token', None)
    if not (self.access_token and self.refresh_token):
        raise build_api_error(response, blob)
    return blob