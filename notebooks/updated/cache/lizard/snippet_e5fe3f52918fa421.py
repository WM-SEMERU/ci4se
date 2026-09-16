def _create_websession(self):
    from socket import AF_INET
    from aiohttp import ClientTimeout, TCPConnector
    _LOGGER.debug('Creating web session')
    conn = TCPConnector(family=AF_INET, limit_per_host=5,
        enable_cleanup_closed=True)
    session_timeout = ClientTimeout(connect=10)
    self._websession = ClientSession(connector=conn, timeout=session_timeout)
    self._supplied_websession = False