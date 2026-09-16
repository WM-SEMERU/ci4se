def update_site(self, client_secret_expires_at=None):
    params = {'oxd_id': self.oxd_id, 'authorization_redirect_uri': self.
        authorization_redirect_uri}
    if client_secret_expires_at:
        params['client_secret_expires_at'] = client_secret_expires_at
    for param in self.opt_params:
        if self.config.get('client', param):
            value = self.config.get('client', param)
            params[param] = value
    for param in self.opt_list_params:
        if self.config.get('client', param):
            value = self.config.get('client', param).split(',')
            params[param] = value
    logger.debug('Sending `update_site` with params %s', params)
    response = self.msgr.request('update_site', **params)
    logger.debug('Received response: %s', response)
    if response['status'] == 'error':
        raise OxdServerError(response['data'])
    return True