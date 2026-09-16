def getOrderedGlyphSet(self):
    compiler = self.context.compiler
    if compiler is not None:
        return compiler.glyphSet
    from ufo2ft.util import makeOfficialGlyphOrder
    glyphSet = self.context.font
    glyphOrder = makeOfficialGlyphOrder(self.context.font)
    return OrderedDict((gn, glyphSet[gn]) for gn in glyphOrder)