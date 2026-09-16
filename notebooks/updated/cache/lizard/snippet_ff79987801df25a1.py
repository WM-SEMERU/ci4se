def type(self, newtype):
    self._type = newtype
    if self.is_multi:
        for sibling in self.multi_rep.siblings:
            sibling._type = newtype