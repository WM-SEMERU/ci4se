def new_session(self):
    body = yield from self._fetch_json(URL_LOGIN, self._new_session_data)
    self.sma_sid = jmespath.search('result.sid', body)
    if self.sma_sid:
        return True
    msg = 'Could not start session, %s, got {}'.format(body)
    if body.get('err'):
        if body.get('err') == 503:
            _LOGGER.error('Max amount of sessions reached')
        else:
            _LOGGER.error(msg, body.get('err'))
    else:
        _LOGGER.error(msg, 'Session ID expected [result.sid]')
    return False