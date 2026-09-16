def edit_finished(self):
    self.hide()
    if isinstance(self.tab_index, int) and self.tab_index >= 0:
        tab_text = to_text_string(self.text())
        self.main.setTabText(self.tab_index, tab_text)
        self.main.sig_change_name.emit(tab_text)