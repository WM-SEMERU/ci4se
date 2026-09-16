def _isCompatible(self, other, reporter):
    layer1 = self
    layer2 = other
    glyphs1 = set(layer1.keys())
    glyphs2 = set(layer2.keys())
    if len(glyphs1) != len(glyphs2):
        reporter.glyphCountDifference = True
        reporter.warning = True
    if len(glyphs1.difference(glyphs2)) != 0:
        reporter.warning = True
        reporter.glyphsMissingFromLayer2 = list(glyphs1.difference(glyphs2))
    if len(glyphs2.difference(glyphs1)) != 0:
        reporter.warning = True
        reporter.glyphsMissingInLayer1 = list(glyphs2.difference(glyphs1))
    for glyphName in sorted(glyphs1.intersection(glyphs2)):
        glyph1 = layer1[glyphName]
        glyph2 = layer2[glyphName]
        glyphCompatibility = glyph1.isCompatible(glyph2)[1]
        if glyphCompatibility.fatal or glyphCompatibility.warning:
            if glyphCompatibility.fatal:
                reporter.fatal = True
            if glyphCompatibility.warning:
                reporter.warning = True
            reporter.glyphs.append(glyphCompatibility)