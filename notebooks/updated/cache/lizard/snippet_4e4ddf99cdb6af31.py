def disable_audit_device(self, path):
    api_path = '/v1/sys/audit/{path}'.format(path=path)
    return self._adapter.delete(url=api_path)