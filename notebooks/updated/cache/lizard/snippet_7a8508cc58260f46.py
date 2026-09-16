def normalizeGlyphLeftMargin(value):
    if not isinstance(value, (int, float)) and value is not None:
        raise TypeError(
            'Glyph left margin must be an :ref:`type-int-float`, not %s.' %
            type(value).__name__)
    return value