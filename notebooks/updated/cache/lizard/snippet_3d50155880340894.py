def equals(self, other):
    if isinstance(other, SSAEvent):
        return self.as_dict() == other.as_dict()
    else:
        raise TypeError('Cannot compare to non-SSAEvent object')