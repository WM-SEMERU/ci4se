def reset(self, initial_document=None, append_to_history=False):
    assert initial_document is None or isinstance(initial_document, Document)
    if append_to_history:
        self.append_to_history()
    initial_document = initial_document or Document()
    self.__cursor_position = initial_document.cursor_position
    self.validation_error = None
    self.validation_state = ValidationState.UNKNOWN
    self.selection_state = None
    self.multiple_cursor_positions = []
    self.preferred_column = None
    self.complete_state = None
    self.yank_nth_arg_state = None
    self.document_before_paste = None
    self.suggestion = None
    self.history_search_text = None
    self._undo_stack = []
    self._redo_stack = []
    self._working_lines = self.history.strings[:]
    self._working_lines.append(initial_document.text)
    self.__working_index = len(self._working_lines) - 1