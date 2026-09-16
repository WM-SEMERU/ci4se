def insertGlyph(self, glyph, name=None):
    if name is None:
        name = glyph.name
    self[name] = glyph