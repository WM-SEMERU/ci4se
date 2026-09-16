def add_source(self, url, **kwargs):
    self['sources'].append(dict(url=url, **kwargs))