def _get_access_token(self, code, **params):
    params.update({'code': code, 'client_id': self.client_id,
        'client_secret': self.secret, 'redirect_uri': self.get_callback_url()})
    logger.debug('Params: %s', params)
    resp, content = self.request_access_token(params=params)
    content = smart_unicode(content)
    logger.debug('Status: %s', resp['status'])
    logger.debug('Content: %s', content)
    content = self.parse_access_token(content)
    if 'error' in content:
        raise OAuthError(_(
            'Received error while obtaining access token from %s: %s') % (
            self.access_token_url, content['error']))
    return content