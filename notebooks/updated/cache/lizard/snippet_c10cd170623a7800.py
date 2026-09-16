def set_footer(self, **kwargs):
    self.footer = {'text': kwargs.get('text'), 'icon_url': kwargs.get(
        'icon_url'), 'proxy_icon_url': kwargs.get('proxy_icon_url')}