def annotate_json(self, text, annotators=None):
    doc = self.annotate(text, annotators)
    return doc.json