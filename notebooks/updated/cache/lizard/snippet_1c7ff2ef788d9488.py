def prepend_urls(self):
    return [url('^(?P<resource_name>%s)/(?P<pk>\\w[\\w/-]*)/generate%s$' %
        (self._meta.resource_name, trailing_slash()), self.wrap_view(
        'generate'), name='api_tileset_generate'), url(
        '^(?P<resource_name>%s)/(?P<pk>\\w[\\w/-]*)/download%s$' % (self.
        _meta.resource_name, trailing_slash()), self.wrap_view('download'),
        name='api_tileset_download'), url(
        '^(?P<resource_name>%s)/(?P<pk>\\w[\\w/-]*)/status%s$' % (self.
        _meta.resource_name, trailing_slash()), self.wrap_view('status'),
        name='api_tileset_status'), url(
        '^(?P<resource_name>%s)/(?P<pk>\\w[\\w/-]*)/stop%s$' % (self._meta.
        resource_name, trailing_slash()), self.wrap_view('stop'), name=
        'api_tileset_stop')]