def on_get(self, req, resp, handler=None, **kwargs):
    self.handle(handler or self.list, req, resp, **kwargs)