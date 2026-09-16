def com_google_fonts_check_linegaps(ttFont):
    if ttFont['hhea'].lineGap != 0:
        yield WARN, Message('hhea', 'hhea lineGap is not equal to 0.')
    elif ttFont['OS/2'].sTypoLineGap != 0:
        yield WARN, Message('OS/2', 'OS/2 sTypoLineGap is not equal to 0.')
    else:
        yield PASS, 'OS/2 sTypoLineGap and hhea lineGap are both 0.'