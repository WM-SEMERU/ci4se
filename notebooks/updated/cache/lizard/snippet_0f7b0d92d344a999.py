def get_stats(self, queue):
    uri = '/%s/%s/stats' % (self.uri_base, utils.get_id(queue))
    resp, resp_body = self.api.method_get(uri)
    return resp_body.get('messages')