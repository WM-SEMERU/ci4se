def get_client_token(self, client_id=None, client_secret=None, op_host=None,
    op_discovery_path=None, scope=None, auto_update=True):
    params = dict(client_id=client_id, client_secret=client_secret, op_host
        =op_host)
    if op_discovery_path:
        params['op_discovery_path'] = op_discovery_path
    if scope and isinstance(scope, list):
        params['scope'] = scope
    if not client_id:
        params['client_id'] = self.config.get('client', 'client_id')
    if not client_secret:
        params['client_secret'] = self.config.get('client', 'client_secret')
    if not op_host:
        params['op_host'] = self.config.get('client', 'op_host')
    logger.debug('Sending command `get_client_token` with params %s', params)
    response = self.msgr.request('get_client_token', **params)
    logger.debug('Received response: %s', response)
    if response['status'] == 'error':
        raise OxdServerError(response['data'])
    self.config.set('client', 'protection_access_token', response['data'][
        'access_token'])
    self.msgr.access_token = response['data']['access_token']
    if auto_update:
        interval = int(response['data']['expires_in'])
        args = [client_id, client_secret, op_host, op_discovery_path, scope,
            auto_update]
        logger.info(
            'Setting up a threading.Timer to get_client_token in %s seconds',
            interval)
        t = Timer(interval, self.get_client_token, args)
        t.start()
    return response['data']