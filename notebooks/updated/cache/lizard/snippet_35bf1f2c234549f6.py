def post(self, url, data=None, json=None, callback=None, retry=0, **kwargs):
    return self.request('post', url=url, data=data, json=json, callback=
        callback, retry=retry, **kwargs)