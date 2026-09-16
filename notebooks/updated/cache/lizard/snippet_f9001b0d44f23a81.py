def find_content(self, text):
    if self.trigraphs:
        text = RE_TRIGRAPHS.sub(self.process_trigraphs, text)
    for m in self.pattern.finditer(self.norm_nl(text)):
        self.evaluate(m)