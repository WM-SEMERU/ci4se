def open(self):
    try:
        if self.transport in ('http', 'https'):
            connection = pyeapi.client.connect(transport=self.transport,
                host=self.hostname, username=self.username, password=self.
                password, port=self.port, timeout=self.timeout)
        elif self.transport == 'socket':
            connection = pyeapi.client.connect(transport=self.transport)
        else:
            raise ConnectionException('Unknown transport: {}'.format(self.
                transport))
        if self.device is None:
            self.device = pyeapi.client.Node(connection, enablepwd=self.
                enablepwd)
        self.device.run_commands(['show clock'], encoding='text')
    except ConnectionError as ce:
        raise ConnectionException(ce.message)