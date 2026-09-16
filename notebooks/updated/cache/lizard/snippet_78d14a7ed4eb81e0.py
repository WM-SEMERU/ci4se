def copy(self, overrides=None, locked=False):
    other = copy.copy(self)
    if overrides is not None:
        other.overrides = overrides
    other.locked = locked
    other._uncache()
    return other