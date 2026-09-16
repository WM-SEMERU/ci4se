def post_object_async(self, path, **kwds):
    return self.do_request_async(self.api_url + path, 'POST', **kwds)