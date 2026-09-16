def makeUnicodeToGlyphNameMapping(self):
    compiler = self.context.compiler
    cmap = None
    if compiler is not None:
        table = compiler.ttFont.get('cmap')
        if table is not None:
            cmap = table.getBestCmap()
    if cmap is None:
        from ufo2ft.util import makeUnicodeToGlyphNameMapping
        if compiler is not None:
            glyphSet = compiler.glyphSet
        else:
            glyphSet = self.context.font
        cmap = makeUnicodeToGlyphNameMapping(glyphSet)
    return cmap