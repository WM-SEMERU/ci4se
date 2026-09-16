def matches(self, other):
    if not isinstance(other, Failure):
        return False
    if self.exc_info is None or other.exc_info is None:
        return self._matches(other)
    else:
        return self == other