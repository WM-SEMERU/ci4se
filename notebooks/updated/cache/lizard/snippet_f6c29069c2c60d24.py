def connect(self, **kw_params):
    if self.connection_cls:
        return self.connection_cls(region=self, **kw_params)