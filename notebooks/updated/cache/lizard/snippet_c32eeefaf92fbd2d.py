def remove(self, *keys):
    dumps = self.pickler.dumps
    self.cache.remove([dumps(v) for v in keys])