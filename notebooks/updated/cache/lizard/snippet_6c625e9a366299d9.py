def add_item(self, item):
    self.beginInsertRows(QtCore.QModelIndex(), self.rowCount(), self.rowCount()
        )
    item['parent'] = self
    item = Item(**item)
    self.items.append(item)
    self.endInsertRows()
    item.__datachanged__.connect(self._dataChanged)
    return item