def reset_spent_time(self, **kwargs):
    path = '%s/%s/reset_spent_time' % (self.manager.path, self.get_id())
    return self.manager.gitlab.http_post(path, **kwargs)