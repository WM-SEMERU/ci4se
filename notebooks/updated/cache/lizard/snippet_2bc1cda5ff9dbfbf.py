def options(self, alias, uri, headers=None, allow_redirects=None, timeout=None
    ):
    logger.warn('Deprecation Warning: Use Options Request in the future')
    session = self._cache.switch(alias)
    redir = True if allow_redirects is None else allow_redirects
    response = self._options_request(session, uri, headers, redir, timeout)
    return response