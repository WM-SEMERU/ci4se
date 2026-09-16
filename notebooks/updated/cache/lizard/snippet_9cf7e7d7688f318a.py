def dragMoveEvent(self, event):
    super(AbstractDragView, self).dragMoveEvent(event)
    if event.mimeData().hasFormat('application/x-protocol'):
        self.dragline = self.cursor(event.pos())
        self.viewport().update()
        event.setDropAction(QtCore.Qt.MoveAction)
        event.accept()
    else:
        event.ignore()