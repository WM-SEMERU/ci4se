def cursor_position_changed(self):
    if self.bracepos is not None:
        self.__highlight(self.bracepos, cancel=True)
        self.bracepos = None
    cursor = self.textCursor()
    if cursor.position() == 0:
        return
    cursor.movePosition(QTextCursor.PreviousCharacter, QTextCursor.KeepAnchor)
    text = to_text_string(cursor.selectedText())
    pos1 = cursor.position()
    if text in (')', ']', '}'):
        pos2 = self.find_brace_match(pos1, text, forward=False)
    elif text in ('(', '[', '{'):
        pos2 = self.find_brace_match(pos1, text, forward=True)
    else:
        return
    if pos2 is not None:
        self.bracepos = pos1, pos2
        self.__highlight(self.bracepos, color=self.matched_p_color)
    else:
        self.bracepos = pos1,
        self.__highlight(self.bracepos, color=self.unmatched_p_color)