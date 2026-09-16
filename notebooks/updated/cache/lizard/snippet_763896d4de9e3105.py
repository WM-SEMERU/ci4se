def set_item(self, index, new_item):
    row = index.row() if hasattr(index, 'row') else index
    self.collection[row] = new_item
    self.dataChanged.emit(self.index(row, 0), self.index(row, self.rowCount
        () - 1))