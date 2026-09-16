def assoc(self, index, value):
    newvec = ImmutableVector()
    newvec.tree = self.tree.assoc(index, value)
    if index >= self._length:
        newvec._length = index + 1
    else:
        newvec._length = self._length
    return newvec