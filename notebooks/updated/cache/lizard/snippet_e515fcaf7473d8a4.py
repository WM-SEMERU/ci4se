def addSubEditor(self, subEditor, isFocusProxy=False):
    self.hBoxLayout.insertWidget(len(self._subEditors), subEditor)
    self._subEditors.append(subEditor)
    subEditor.installEventFilter(self)
    subEditor.setFocusPolicy(Qt.StrongFocus)
    if isFocusProxy:
        self.setFocusProxy(subEditor)
    return subEditor