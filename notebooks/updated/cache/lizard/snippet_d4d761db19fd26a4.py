def _set_history_search(self):
    if self.enable_history_search():
        if self.history_search_text is None:
            self.history_search_text = self.document.text_before_cursor
    else:
        self.history_search_text = None