def obj(self):
    if self._wrapped is not self.Null:
        return self._wrapped
    else:
        return self.object