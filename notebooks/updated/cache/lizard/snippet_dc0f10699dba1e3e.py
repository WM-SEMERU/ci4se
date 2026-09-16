def perform_word_selection(self, event=None):
    self.editor.setTextCursor(TextHelper(self.editor).word_under_cursor(True))
    if event:
        event.accept()