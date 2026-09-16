def image(self):
    uri = '/%s/image' % self.uri_base
    resp, resp_body = self.api.method_get(uri)
    return resp_body