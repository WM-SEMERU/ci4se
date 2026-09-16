def viewportEvent(self, event):
    if event.type() == event.ToolTip and self.usePopupToolTip():
        index = self.indexAt(event.pos())
        item = self.itemAt(event.pos())
        if not (index and item):
            event.ignore()
            return False
        tip = item.toolTip(index.column())
        rect = self.visualRect(index)
        point = QtCore.QPoint(rect.left() + 5, rect.bottom() + 1)
        point = self.viewport().mapToGlobal(point)
        if tip:
            XPopupWidget.showToolTip(tip, anchor=XPopupWidget.Anchor.
                TopLeft, point=point, parent=self)
        event.accept()
        return True
    else:
        return super(XTreeWidget, self).viewportEvent(event)