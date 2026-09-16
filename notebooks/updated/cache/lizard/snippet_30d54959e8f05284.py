def get(self, name):
    attr = getattr(self.context, name, None)
    if callable(attr):
        return attr()
    return attr