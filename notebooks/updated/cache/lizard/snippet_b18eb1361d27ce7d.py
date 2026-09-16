def image_tasks(self):
    uri = '/%s/tasks' % self.uri_base
    resp, resp_body = self.api.method_get(uri)
    return resp_body