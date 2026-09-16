def setupTable_hmtx(self):
    if 'hmtx' not in self.tables:
        return
    self.otf['hmtx'] = hmtx = newTable('hmtx')
    hmtx.metrics = {}
    for glyphName, glyph in self.allGlyphs.items():
        width = otRound(glyph.width)
        if width < 0:
            raise ValueError("The width should not be negative: '%s'" %
                glyphName)
        bounds = self.glyphBoundingBoxes[glyphName]
        left = bounds.xMin if bounds else 0
        hmtx[glyphName] = width, left