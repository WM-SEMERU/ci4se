def _copy(self, other, copy_func):
    super(Constructable, self)._copy(other, copy_func)
    self.method = other.method
    self._indefinite = other._indefinite