def on_state_changed(self, state):
    if state:
        self.editor.key_pressed.connect(self._on_key_pressed)
        if self._highlight_caret:
            self.editor.cursorPositionChanged.connect(self.
                _highlight_caret_scope)
            self._block_nbr = -1
        self.editor.new_text_set.connect(self._clear_block_deco)
    else:
        self.editor.key_pressed.disconnect(self._on_key_pressed)
        if self._highlight_caret:
            self.editor.cursorPositionChanged.disconnect(self.
                _highlight_caret_scope)
            self._block_nbr = -1
        self.editor.new_text_set.disconnect(self._clear_block_deco)