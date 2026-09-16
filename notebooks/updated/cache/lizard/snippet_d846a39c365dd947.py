def set_source_text(self, p_text):
    self.src = p_text.strip()
    self.fields = parse_line(self.src)