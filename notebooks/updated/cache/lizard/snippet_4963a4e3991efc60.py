def when(self, *bools):
    self.passes = self.passes and all(bools)
    return self