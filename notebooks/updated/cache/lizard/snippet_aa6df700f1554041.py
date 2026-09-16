def create_token_response(self, request, token_handler):
    headers = self._get_default_headers()
    try:
        self.validate_token_request(request)
        log.debug('Token request validation ok for %r.', request)
    except errors.OAuth2Error as e:
        log.debug('Client error during validation of %r. %r.', request, e)
        headers.update(e.headers)
        return headers, e.json, e.status_code
    token = token_handler.create_token(request, refresh_token=self.
        refresh_token)
    for modifier in self._token_modifiers:
        token = modifier(token, token_handler, request)
    self.request_validator.save_token(token, request)
    self.request_validator.invalidate_authorization_code(request.client_id,
        request.code, request)
    return headers, json.dumps(token), 200