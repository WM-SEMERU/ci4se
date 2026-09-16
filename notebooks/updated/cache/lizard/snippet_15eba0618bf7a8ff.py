def patch(self, url, data=None, params=None):
    return self.request('patch', url, data, params)