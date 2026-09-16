def filter(self, object, *args, **kw):
    for plugin in self.plugins:
        object = plugin.handle(object, *args, **kw)
        if object is None:
            return object
    return object