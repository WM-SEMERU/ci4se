def go_to_new_line(self):
    self.stdkey_end(False, False)
    self.insert_text(self.get_line_separator())