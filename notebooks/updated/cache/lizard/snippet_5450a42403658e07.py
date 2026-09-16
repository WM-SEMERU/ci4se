def insert(self, index, key, value):
    if key in self.keyOrder:
        n = self.keyOrder.index(key)
        del self.keyOrder[n]
        if n < index:
            index -= 1
    self.keyOrder.insert(index, key)
    super(SortedDict, self).__setitem__(key, value)