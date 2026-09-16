def set_thumbnail(self, **kwargs):
    self.thumbnail = {'url': kwargs.get('url'), 'proxy_url': kwargs.get(
        'proxy_url'), 'height': kwargs.get('height'), 'width': kwargs.get(
        'width')}