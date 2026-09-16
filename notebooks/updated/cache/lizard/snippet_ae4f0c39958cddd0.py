def forward(self, method, type, path, data=None):
    try:
        action = '/{}/{}'.format(type, path)
        res = yield from self.http_query(method, action, data=data, timeout
            =None)
    except aiohttp.ServerDisconnectedError:
        log.error('Connection lost to %s during %s %s', self._id, method,
            action)
        raise aiohttp.web.HTTPGatewayTimeout()
    return res.json