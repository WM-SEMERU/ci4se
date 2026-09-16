def make_request(self, resource, params=None):
    return super(VideoApi, self).make_request('video/%s' % resource, params)