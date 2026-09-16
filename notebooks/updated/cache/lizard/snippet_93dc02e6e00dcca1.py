def compileTTF(ufo, preProcessorClass=TTFPreProcessor, outlineCompilerClass
    =OutlineTTFCompiler, featureCompilerClass=None, featureWriters=None,
    glyphOrder=None, useProductionNames=None, convertCubics=True,
    cubicConversionError=None, reverseDirection=True, rememberCurveType=
    True, removeOverlaps=False, overlapsBackend=None, inplace=False,
    layerName=None, skipExportGlyphs=None):
    logger.info('Pre-processing glyphs')
    if skipExportGlyphs is None:
        skipExportGlyphs = ufo.lib.get('public.skipExportGlyphs', [])
    preProcessor = preProcessorClass(ufo, inplace=inplace, removeOverlaps=
        removeOverlaps, overlapsBackend=overlapsBackend, convertCubics=
        convertCubics, conversionError=cubicConversionError,
        reverseDirection=reverseDirection, rememberCurveType=
        rememberCurveType, layerName=layerName, skipExportGlyphs=
        skipExportGlyphs)
    glyphSet = preProcessor.process()
    logger.info('Building OpenType tables')
    outlineCompiler = outlineCompilerClass(ufo, glyphSet=glyphSet,
        glyphOrder=glyphOrder)
    otf = outlineCompiler.compile()
    if layerName is None:
        compileFeatures(ufo, otf, glyphSet=glyphSet, featureWriters=
            featureWriters, featureCompilerClass=featureCompilerClass)
    postProcessor = PostProcessor(otf, ufo, glyphSet=glyphSet)
    otf = postProcessor.process(useProductionNames)
    return otf