def raw_pull(self, topic):
    assert topic is not None, 'A topic of None is not allowed'
    kwargs = {} if not self.user else {'auth': (self.user, self.token)}
    my_req = requests.get('%s/issues/%s' % (self.base_url, topic), **kwargs)
    return my_req