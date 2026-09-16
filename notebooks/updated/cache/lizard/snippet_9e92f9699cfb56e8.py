def mirror_pull(self, **kwargs):
    path = '/projects/%s/mirror/pull' % self.get_id()
    self.manager.gitlab.http_post(path, **kwargs)