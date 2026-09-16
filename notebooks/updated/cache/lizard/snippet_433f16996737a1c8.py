def document(self):
    return self._document_cache[self.text, self.cursor_position, self.
        selection_state]