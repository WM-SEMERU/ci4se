def diff(self, **kwargs):
    path = '%s/%s/diff' % (self.manager.path, self.get_id())
    return self.manager.gitlab.http_get(path, **kwargs)