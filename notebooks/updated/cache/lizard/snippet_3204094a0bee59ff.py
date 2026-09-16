def lang(self, lang):
    self.graph.set((self.asNode(), DC.language, Literal(lang)))