def filter(self, *args):
    if len(args) == 1 and isinstance(args[0], Filter):
        filter = args[0]
    else:
        filter = Filter(*args)
    filter.object_getattr = self.object_getattr
    self.filters.append(filter)
    return self