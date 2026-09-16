def todo(self, **kwargs):
    path = '%s/%s/todo' % (self.manager.path, self.get_id())
    self.manager.gitlab.http_post(path, **kwargs)