def get_partial_word_under_cursor(self):
    if not re.match('^\\w+$', foundations.strings.to_string(self.
        get_previous_character())):
        return QString()
    cursor = self.textCursor()
    position = cursor.position()
    cursor.movePosition(QTextCursor.PreviousWord, QTextCursor.KeepAnchor)
    return cursor.selectedText()