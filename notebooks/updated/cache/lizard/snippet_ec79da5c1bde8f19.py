def perform_matched_selection(self, event):
    selected = TextHelper(self.editor).match_select()
    if selected and event:
        event.accept()