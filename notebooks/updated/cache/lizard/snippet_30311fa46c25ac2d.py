def history(self, **kwargs):
    url_str = self.base_url + '/%s/state-history' % kwargs['alarm_id']
    del kwargs['alarm_id']
    if kwargs:
        url_str = url_str + '?%s' % parse.urlencode(kwargs, True)
    resp = self.client.list(url_str)
    return resp['elements'] if type(resp) is dict else resp