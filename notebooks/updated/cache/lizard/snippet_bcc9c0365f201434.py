def post(self, url, data=None, **kwargs):
    return self.oauth_request(url, 'post', data=data, **kwargs)