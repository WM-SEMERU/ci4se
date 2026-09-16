def closed_by(self, **kwargs):
    path = '%s/%s/closed_by' % (self.manager.path, self.get_id())
    return self.manager.gitlab.http_get(path, **kwargs)