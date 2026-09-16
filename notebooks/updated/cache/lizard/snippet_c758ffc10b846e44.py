def create_role(self, role_name, mount_point='approle', **kwargs):
    return self._adapter.post('/v1/auth/{0}/role/{1}'.format(mount_point,
        role_name), json=kwargs)