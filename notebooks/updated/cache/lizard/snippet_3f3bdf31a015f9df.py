def contained_by(self, *args):
    self.op = '<@'
    self.negate_op = None
    self.value = self._array_value(args)
    return self