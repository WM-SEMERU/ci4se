def get_params(self):
    param_names = ['aws_access_key_id', 'aws_secret_access_key',
        'is_secure', 'port', 'proxy', 'proxy_port', 'proxy_user',
        'proxy_pass', 'debug', 'https_connection_factory']
    params = {}
    for name in param_names:
        params[name] = getattr(self, name)
    return params