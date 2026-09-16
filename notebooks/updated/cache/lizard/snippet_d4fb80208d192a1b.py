def notify(self, method, params=None):
    log.debug('Sending notification: %s %s', method, params)
    message = {'jsonrpc': JSONRPC_VERSION, 'method': method}
    if params is not None:
        message['params'] = params
    self._consumer(message)