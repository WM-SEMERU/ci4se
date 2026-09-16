def eventFilter(self, object, event):
    if event.type() == event.KeyPress:
        if event.key() == Qt.Key_Escape:
            self._completer.hide()
            self._completer.setCurrentItem(None)
        elif event.key() in (Qt.Key_Enter, Qt.Key_Return):
            tree = self._completer
            item = tree.currentItem() or tree.itemAt(0, 0)
            self.triggerItem(item)
        self._searchEdit.keyPressEvent(event)
    return False