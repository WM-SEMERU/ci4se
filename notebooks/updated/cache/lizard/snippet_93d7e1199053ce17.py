def when(self, key):
    ctx = Context(key, self)
    self.context.append(ctx)
    return ctx