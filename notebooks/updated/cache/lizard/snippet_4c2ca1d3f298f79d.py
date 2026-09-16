def updateCheckedText(self):
    if not self.isCheckable():
        return
    indexes = self.checkedIndexes()
    items = self.checkedItems()
    if len(items) < 2 or self.separator():
        self.lineEdit().setText(self.separator().join(items))
    else:
        self.lineEdit().setText('{0} items selected'.format(len(items)))
    if not self.signalsBlocked():
        self.checkedItemsChanged.emit(items)
        self.checkedIndexesChanged.emit(indexes)