def com_google_fonts_check_os2_metrics_match_hhea(ttFont):
    if ttFont['OS/2'].sTypoAscender != ttFont['hhea'].ascent:
        yield FAIL, Message('ascender',
            'OS/2 sTypoAscender and hhea ascent must be equal.')
    elif ttFont['OS/2'].sTypoDescender != ttFont['hhea'].descent:
        yield FAIL, Message('descender',
            'OS/2 sTypoDescender and hhea descent must be equal.')
    else:
        yield PASS, 'OS/2.sTypoAscender/Descender values match hhea.ascent/descent.'