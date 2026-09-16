def mark_whole_doc_dirty(self):
    text_cursor = self._editor.textCursor()
    text_cursor.select(text_cursor.Document)
    self._editor.document().markContentsDirty(text_cursor.selectionStart(),
        text_cursor.selectionEnd())