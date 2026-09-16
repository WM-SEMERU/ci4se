def get_logout_uri(self, id_token_hint=None, post_logout_redirect_uri=None,
    state=None, session_state=None):
    params = {'oxd_id': self.oxd_id}
    if id_token_hint:
        params['id_token_hint'] = id_token_hint
    if post_logout_redirect_uri:
        params['post_logout_redirect_uri'] = post_logout_redirect_uri
    if state:
        params['state'] = state
    if session_state:
        params['session_state'] = session_state
    logger.debug('Sending command `get_logout_uri` with params %s', params)
    response = self.msgr.request('get_logout_uri', **params)
    logger.debug('Received response: %s', response)
    if response['status'] == 'error':
        raise OxdServerError(response['data'])
    return response['data']['uri']