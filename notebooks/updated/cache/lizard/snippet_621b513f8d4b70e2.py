def openTypeOS2TypoLineGapFallback(info):
    return max(int(info.unitsPerEm * 1.2) - info.ascender + info.descender, 0)