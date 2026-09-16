def makeFontBoundingBox(self):
    if not hasattr(self, 'glyphBoundingBoxes'):
        self.glyphBoundingBoxes = self.makeGlyphsBoundingBoxes()
    fontBox = None
    for glyphName, glyphBox in self.glyphBoundingBoxes.items():
        if glyphBox is None:
            continue
        if fontBox is None:
            fontBox = glyphBox
        else:
            fontBox = unionRect(fontBox, glyphBox)
    if fontBox is None:
        fontBox = BoundingBox(0, 0, 0, 0)
    return fontBox