def remove(self, child):
    if not isinstance(child, AbstractElement):
        raise ValueError('Expected AbstractElement, got ' + str(type(child)))
    if child.parent == self:
        child.parent = None
    self.data.remove(child)
    if child.id and self.doc and child.id in self.doc.index:
        del self.doc.index[child.id]