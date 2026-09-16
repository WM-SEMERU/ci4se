def _log_in(self):
    username = (self._request.url_info.username or self._request.username or
        'anonymous')
    password = (self._request.url_info.password or self._request.password or
        '-wpull@')
    cached_login = self._login_table.get(self._control_connection)
    if cached_login and cached_login == (username, password):
        _logger.debug('Reusing existing login.')
        return
    try:
        yield from self._commander.login(username, password)
    except FTPServerError as error:
        raise AuthenticationError('Login error: {}'.format(error)) from error
    self._login_table[self._control_connection] = username, password