def enable_secrets_engine(self, backend_type, path=None, description=None,
    config=None, plugin_name=None, options=None, local=False, seal_wrap=False):
    if path is None:
        path = backend_type
    params = {'type': backend_type, 'description': description, 'config':
        config, 'options': options, 'plugin_name': plugin_name, 'local':
        local, 'seal_wrap': seal_wrap}
    api_path = '/v1/sys/mounts/{path}'.format(path=path)
    return self._adapter.post(url=api_path, json=params)