def start_selection(self, selection_type=SelectionType.CHARACTERS):
    self.selection_state = SelectionState(self.cursor_position, selection_type)