def eventFilter(self, object, event):
    if event.type() == QEvent.KeyPress and event.modifiers() == Qt.NoModifier:
        if event.key() == Qt.Key_Escape:
            self.closeMe.emit()
            return True
        elif event.key() == Qt.Key_Down:
            if self._selectedIndex + 1 < self.model().rowCount():
                self._selectItem(self._selectedIndex + 1)
            return True
        elif event.key() == Qt.Key_Up:
            if self._selectedIndex - 1 >= 0:
                self._selectItem(self._selectedIndex - 1)
            return True
        elif event.key() in (Qt.Key_Enter, Qt.Key_Return):
            if self._selectedIndex != -1:
                self.itemSelected.emit(self._selectedIndex)
                return True
        elif event.key() == Qt.Key_Tab:
            self.tabPressed.emit()
            return True
    elif event.type() == QEvent.FocusOut:
        self.closeMe.emit()
    return False