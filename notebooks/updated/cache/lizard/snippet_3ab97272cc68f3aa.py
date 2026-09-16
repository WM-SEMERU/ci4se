def typeSort(self):
    self.children.sort()
    for c in self.children:
        c.typeSort()