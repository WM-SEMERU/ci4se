def sortByColumn(self, index, direction):
    if self.isPaged() and not self.isFullyLoaded():
        self.reorder(index, direction)
    else:
        super(XOrbTreeWidget, self).sortByColumn(index, direction)