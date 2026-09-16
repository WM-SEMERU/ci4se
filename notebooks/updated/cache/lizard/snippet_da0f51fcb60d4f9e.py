def set_proxy(self, host, port, user, password):
    if user and password:
        proxy_string = '{}:{}@{}:{}'.format(user, password, host, port)
    else:
        proxy_string = '{}:{}'.format(host, port)
    self.proxies = {'http': 'http://{}'.format(proxy_string), 'https':
        'https://{}'.format(proxy_string)}