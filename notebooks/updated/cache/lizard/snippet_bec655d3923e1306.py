def _update_proxy(self, change):
    if change['type'] == 'event':
        name = 'do_' + change['name']
        if hasattr(self.proxy, name):
            handler = getattr(self.proxy, name)
            handler()
    else:
        super(WebView, self)._update_proxy(change)