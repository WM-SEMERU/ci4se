def process_part(self, char):
    if char in self.whitespace or char == self.eol_char:
        self.parts.append(''.join(self.part))
        self.part = []
        self.process_char = self.process_delimiter
        if char == self.eol_char:
            self.complete = True
        return
    if char in self.quote_chars:
        self.inquote = char
        self.process_char = self.process_quote
        return
    self.part.append(char)