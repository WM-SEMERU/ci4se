def get_server_url(self):
    server_host = self.driver_wrapper.config.get('Server', 'host')
    server_port = self.driver_wrapper.config.get('Server', 'port')
    server_username = self.driver_wrapper.config.get_optional('Server',
        'username')
    server_password = self.driver_wrapper.config.get_optional('Server',
        'password')
    server_auth = '{}:{}@'.format(server_username, server_password
        ) if server_username and server_password else ''
    server_url = 'http://{}{}:{}'.format(server_auth, server_host, server_port)
    return server_url