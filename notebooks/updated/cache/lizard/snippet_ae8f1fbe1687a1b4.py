def _translate_category(glyph_name, unicode_category):
    DEFAULT_CATEGORIES = {None: ('Letter', None), 'Cc': ('Separator', None),
        'Cf': ('Separator', 'Format'), 'Cn': ('Symbol', None), 'Co': (
        'Letter', 'Compatibility'), 'Ll': ('Letter', 'Lowercase'), 'Lm': (
        'Letter', 'Modifier'), 'Lo': ('Letter', None), 'Lt': ('Letter',
        'Uppercase'), 'Lu': ('Letter', 'Uppercase'), 'Mc': ('Mark',
        'Spacing Combining'), 'Me': ('Mark', 'Enclosing'), 'Mn': ('Mark',
        'Nonspacing'), 'Nd': ('Number', 'Decimal Digit'), 'Nl': ('Number',
        None), 'No': ('Number', 'Decimal Digit'), 'Pc': ('Punctuation',
        None), 'Pd': ('Punctuation', 'Dash'), 'Pe': ('Punctuation',
        'Parenthesis'), 'Pf': ('Punctuation', 'Quote'), 'Pi': (
        'Punctuation', 'Quote'), 'Po': ('Punctuation', None), 'Ps': (
        'Punctuation', 'Parenthesis'), 'Sc': ('Symbol', 'Currency'), 'Sk':
        ('Mark', 'Spacing'), 'Sm': ('Symbol', 'Math'), 'So': ('Symbol',
        None), 'Zl': ('Separator', None), 'Zp': ('Separator', None), 'Zs':
        ('Separator', 'Space')}
    glyphs_category = DEFAULT_CATEGORIES.get(unicode_category, ('Letter', None)
        )
    if '_' in glyph_name and glyphs_category[0] != 'Mark':
        return glyphs_category[0], 'Ligature'
    return glyphs_category