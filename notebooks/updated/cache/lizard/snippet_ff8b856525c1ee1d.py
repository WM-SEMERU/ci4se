def set_text(self, text):
    text = text.strip()
    new_text = self.text() + text
    self.setText(new_text)