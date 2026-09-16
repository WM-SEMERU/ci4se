def showPopup(self):
    if not self.showTreePopup():
        return super(XOrbRecordBox, self).showPopup()
    tree = self.treePopupWidget()
    if tree and not tree.isVisible():
        tree.move(self.mapToGlobal(QPoint(0, self.height())))
        tree.resize(self.width(), 250)
        tree.resizeToContents()
        tree.filterItems('')
        tree.setFilteredColumns(range(tree.columnCount()))
        tree.show()