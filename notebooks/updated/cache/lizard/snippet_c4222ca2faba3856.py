def update(self, incr=1, force=False):
    self.count += incr
    self.parent.update(incr, force)