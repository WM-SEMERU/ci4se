def add(self, *args, **kargs):
    self.invalidate_cache()
    self.routes.append(self.make_route(*args, **kargs))