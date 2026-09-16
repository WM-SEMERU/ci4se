def slt(self, other):
    self._check_match(other)
    return self.to_sint() < other.to_sint()