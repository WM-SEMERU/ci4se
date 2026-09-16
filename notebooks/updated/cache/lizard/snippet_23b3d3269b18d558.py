def setParent(self, other):
    if self._parent == other:
        return False
    if self._parent and self in self._parent._children:
        self._parent._children.remove(self)
    self._parent = other
    if self._parent and not self in self._children:
        self._parent._children.append(self)
    self.sync()
    return True