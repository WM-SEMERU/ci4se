def set(self, name, value, feature_group=None, user=None, **kwargs):
    path = '%s/%s' % (self.path, name.replace('/', '%2F'))
    data = {'value': value, 'feature_group': feature_group, 'user': user}
    server_data = self.gitlab.http_post(path, post_data=data, **kwargs)
    return self._obj_cls(self, server_data)