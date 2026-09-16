def visualRect(self, index):
    rect = super(XTreeWidget, self).visualRect(index)
    item = self.itemFromIndex(index)
    if not rect.isNull() and item and item.isFirstColumnSpanned():
        vpos = self.viewport().mapFromParent(QtCore.QPoint(0, 0))
        rect.setX(vpos.x())
        rect.setWidth(self.width())
        return rect
    return rect