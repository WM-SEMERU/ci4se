def wait(self):

    @param_to_property(action=['exists', 'gone'])
    def _wait(action, timeout=3000):
        if timeout / 1000 + 5 > int(os.environ.get('JSONRPC_TIMEOUT', 90)):
            http_timeout = timeout / 1000 + 5
        else:
            http_timeout = int(os.environ.get('JSONRPC_TIMEOUT', 90))
        method = (self.device.server.jsonrpc_wrap(timeout=http_timeout).
            waitUntilGone if action == 'gone' else self.device.server.
            jsonrpc_wrap(timeout=http_timeout).waitForExists)
        return method(self.selector, timeout)
    return _wait