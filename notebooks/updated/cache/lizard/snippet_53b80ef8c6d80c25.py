def add_text(self, text):
    for char in text:
        self.add_char(char)
    self.flush()