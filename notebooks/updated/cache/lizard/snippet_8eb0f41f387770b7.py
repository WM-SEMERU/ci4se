def diff_config(self, second_host, mode='stanza'):
    second_conn = manager.connect(host=second_host, port=self.port,
        username=self.username, password=self.password, timeout=self.
        connect_timeout, device_params={'name': 'junos'}, hostkey_verify=False)
    command = 'show configuration'
    if mode == 'set':
        command += ' | display set'
    config1 = self._session.command(command, format='text')
    config1 = ''.join([snippet.text.lstrip('\n') for snippet in config1.
        xpath('//configuration-output')])
    config2 = second_conn.command(command, format='text')
    config2 = ''.join([snippet.text.lstrip('\n') for snippet in config2.
        xpath('//configuration-output')])
    return difflib.unified_diff(config1.splitlines(), config2.splitlines(),
        self.host, second_host)