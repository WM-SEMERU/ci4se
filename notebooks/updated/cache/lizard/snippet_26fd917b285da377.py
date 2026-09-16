def get_authentication_tokens(self, callback_url=None, force_login=False,
    screen_name=''):
    if self.oauth_version != 1:
        raise TwythonError(
            'This method can only be called when your                                OAuth version is 1.0.'
            )
    request_args = {}
    if callback_url:
        request_args['oauth_callback'] = callback_url
    response = self.client.get(self.request_token_url, params=request_args)
    if response.status_code == 401:
        raise TwythonAuthError(response.content, error_code=response.
            status_code)
    elif response.status_code != 200:
        raise TwythonError(response.content, error_code=response.status_code)
    request_tokens = dict(parse_qsl(response.content.decode('utf-8')))
    if not request_tokens:
        raise TwythonError('Unable to decode request tokens.')
    oauth_callback_confirmed = request_tokens.get('oauth_callback_confirmed'
        ) == 'true'
    auth_url_params = {'oauth_token': request_tokens['oauth_token']}
    if force_login:
        auth_url_params.update({'force_login': force_login, 'screen_name':
            screen_name})
    if callback_url and not oauth_callback_confirmed:
        auth_url_params['oauth_callback'] = self.callback_url
    request_tokens['auth_url'] = self.authenticate_url + '?' + urlencode(
        auth_url_params)
    return request_tokens