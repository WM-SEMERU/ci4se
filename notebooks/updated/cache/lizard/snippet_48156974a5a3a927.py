def insert_line_below(self, copy_margin=True):
    if copy_margin:
        insert = '\n' + self.document.leading_whitespace_in_current_line
    else:
        insert = '\n'
    self.cursor_position += self.document.get_end_of_line_position()
    self.insert_text(insert)