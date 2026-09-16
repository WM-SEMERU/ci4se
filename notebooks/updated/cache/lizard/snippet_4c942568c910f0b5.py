def _debug_info(self):
    self._msg('DEBUG')
    self._msg2('WorkDir: {0}'.format(self._curdir))
    self._msg2('Cookies: {0}'.format(self._session.cookies))
    self._msg2('Headers: {0}'.format(self._session.headers))
    self._msg2('Configs: {0}'.format(self._config))
    self._msg2('Customs: {0}'.format(self._custom))
    self._msg2('Account: {0}'.format(self._account))