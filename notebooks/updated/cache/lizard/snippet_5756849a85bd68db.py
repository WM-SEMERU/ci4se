def commit(self):
    tc = self.qteWidget.textCursor()
    if self.cursorPos0 is None:
        self.cursorPos0 = tc.position()
        self.selText = tc.selection().toHtml()
        self.selStart = tc.selectionStart()
        self.selEnd = tc.selectionEnd()
    else:
        tc.setPosition(self.cursorPos0, QtGui.QTextCursor.MoveAnchor)
    tc.setPosition(self.selStart, QtGui.QTextCursor.MoveAnchor)
    tc.setPosition(self.selEnd, QtGui.QTextCursor.KeepAnchor)
    tc.removeSelectedText()
    if len(self.selText) > 0:
        pos = self.selStart
    else:
        pos = tc.position()
    tc.setPosition(pos)
    self.cursorPos1 = tc.position()
    tc.insertText(self.text)
    self.cursorPos2 = tc.position()
    self.qteWidget.setTextCursor(tc)