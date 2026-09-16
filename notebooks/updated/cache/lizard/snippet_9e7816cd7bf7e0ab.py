def set_permission(self, path, **kwargs):
    response = self._put(path, 'SETPERMISSION', **kwargs)
    assert not response.content