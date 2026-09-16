def enable_audit_device(self, device_type, description=None, options=None,
    path=None):
    if path is None:
        path = device_type
    params = {'type': device_type, 'description': description, 'options':
        options}
    api_path = '/v1/sys/audit/{path}'.format(path=path)
    return self._adapter.post(url=api_path, json=params)