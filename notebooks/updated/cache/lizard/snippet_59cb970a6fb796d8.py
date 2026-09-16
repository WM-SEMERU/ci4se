def _erase_in_line(self, value):
    initial_pos = self._cursor.position()
    if value == 0:
        self._cursor.movePosition(self._cursor.EndOfBlock, self._cursor.
            KeepAnchor)
    elif value == 1:
        self._cursor.movePosition(self._cursor.StartOfBlock, self._cursor.
            KeepAnchor)
    else:
        self._cursor.movePosition(self._cursor.StartOfBlock)
        self._cursor.movePosition(self._cursor.EndOfBlock, self._cursor.
            KeepAnchor)
    self._cursor.insertText(' ' * len(self._cursor.selectedText()))
    self._cursor.setPosition(initial_pos)
    self._text_edit.setTextCursor(self._cursor)
    self._last_cursor_pos = self._cursor.position()